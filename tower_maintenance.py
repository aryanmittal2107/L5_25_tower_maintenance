
"""Track telecom tower maintenance and assess service risks."""

import logging
import sqlite3


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class TowerMaintenance:
    """Manage tower records, servicing, overdue sites, and risk levels."""

    def __init__(self):
        """Initialize the in-memory database and service counter."""
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute(
            """
            CREATE TABLE towers (
                id INTEGER PRIMARY KEY,
                site TEXT,
                last_service INTEGER,
                faults INTEGER
            )
            """
        )
        self.service_count = 0

    def add_tower(self, site, last_service, faults=0):
        """Add a tower with its last service year and fault count."""
        if not isinstance(site, str) or not site.strip():
            raise ValueError("Site name must be a non-empty string.")
        if not isinstance(last_service, int):
            raise ValueError("Last service year must be an integer.")
        if not isinstance(faults, int) or faults < 0:
            raise ValueError("Fault count must be a non-negative integer.")

        try:
            self.conn.execute(
                """
                INSERT INTO towers (site, last_service, faults)
                VALUES (?, ?, ?)
                """,
                (site, last_service, faults),
            )
            self.conn.commit()
        except sqlite3.Error:
            self.conn.rollback()
            logging.exception("Failed to add tower %s", site)
            raise

    def service_tower(self, tower_id, year):
        """Record a tower service and reset its fault count."""
        try:
            cursor = self.conn.execute(
                """
                UPDATE towers
                SET last_service = ?, faults = 0
                WHERE id = ?
                """,
                (year, tower_id),
            )
            self.conn.commit()

            if cursor.rowcount > 0:
                self.service_count += 1
            else:
                logging.warning("Tower ID %s was not found.", tower_id)
        except sqlite3.Error:
            self.conn.rollback()
            logging.exception("Service failed for tower ID %s", tower_id)

    def overdue(self, year):
        """Return sites not serviced for at least two years."""
        rows = self.conn.execute(
            "SELECT site, last_service FROM towers"
        ).fetchall()

        return [
            site
            for site, last_service in rows
            if year - last_service >= 2
        ]

    def risk_level(self, tower_id):
        """Return a tower's risk level based on its fault count."""
        row = self.conn.execute(
            "SELECT faults FROM towers WHERE id = ?",
            (tower_id,),
        ).fetchone()

        if row is None:
            return "unknown"

        if row[0] > 3:
            return "high"
        return "normal"

    def snapshot(self):
        """Return a snapshot of all tower records."""
        return self.conn.execute(
            "SELECT * FROM towers"
        ).fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()


def main():
    """Demonstrate the tower maintenance system."""
    maintenance = TowerMaintenance()

    try:
        maintenance.add_tower("Ridge-A", 2021, 5)
        maintenance.add_tower("Coast-B", 2024)
        maintenance.service_tower(2, 2025)

        total = len(maintenance.snapshot())
        print(
            maintenance.overdue(2025),
            maintenance.risk_level(1),
            total,
            maintenance.service_count,
        )
    finally:
        maintenance.close()


if __name__ == "__main__":
    main()

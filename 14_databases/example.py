"""
Example usage of the database models and CRUD operations.

This demonstrates how to use the database functionality.
"""

from database import create_tables
from crud import (
    add_author,
    get_author_by_id,
    get_all_authors,
    search_authors_by_name,
    update_author,
    delete_author
)


def main():
    """Main example demonstrating CRUD operations."""
    print("=" * 60)
    print("Library Database System - Example Usage")
    print("=" * 60)
    
    # Create tables (only needed once, or when models change)
    print("\n1. Creating database tables...")
    create_tables()
    
    # CREATE - Add authors
    print("\n2. Adding authors...")
    add_author("AUTH001", "Jane Austen", "jane@email.com", "United Kingdom")
    add_author("AUTH002", "Charles Dickens", "charles@email.com", "United Kingdom")
    add_author("AUTH003", "Mark Twain", "mark@email.com", "United States")
    
    # READ - Get all authors
    print("\n3. All authors:")
    authors = get_all_authors()
    for author in authors:
        print(f"  {author.author_id}: {author.name} ({author.country})")
    
    # READ - Get author by ID
    print("\n4. Getting author by ID:")
    author = get_author_by_id("AUTH001")
    if author:
        print(f"  Found: {author.name} - {author.email}")
    
    # READ - Search authors
    print("\n5. Searching for 'Austen':")
    results = search_authors_by_name("Austen")
    for author in results:
        print(f"  Found: {author.name}")
    
    # UPDATE - Modify author
    print("\n6. Updating author...")
    update_author("AUTH001", country="England")
    
    # Verify update
    author = get_author_by_id("AUTH001")
    if author:
        print(f"  Updated: {author.name} - {author.country}")
    
    # DELETE - Remove author (commented out to keep data)
    # print("\n7. Deleting author...")
    # delete_author("AUTH003")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

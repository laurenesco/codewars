# https://www.codewars.com/kata/515bb423de843ea99400000a 

class PaginationHelper:
    

    def __init__(self, collection: list[str], items_per_page: int) -> None:
        """
        Initializes the PaginationHelper object
        """
        self.items_per_page = items_per_page
        self.items = len(collection)
        self.paginated: list[list[str]] = []
        self._paginate_collection(collection)

    def _paginate_collection(self, collection: list[str]) -> None:
        """
        Creates a paginated version of the provided collection as a nested list.
        """
        self.paginated = [
            collection[i:i + self.items_per_page]
            for i in range(0, len(collection), self.items_per_page)
        ]
                    
    def item_count(self) -> int:
        """
        Returns the amount of items in all pages
        """
        return self.items
    
    def page_count(self) -> int:
        """
        Returns amount of pages in paginated result
        """
        return len(self.paginated)
    
    def page_item_count(self, page_index: int) -> int:
        """
        Returns the number of items on the given page. Returns -1 for out of range indices.
        """
        if page_index < 0:
            return -1 
        
        try:
            return len(self.paginated[page_index])
        except IndexError:
            return -1
            
    def page_index(self, item_index: int) -> int:
        """
        Determines what page the item of the given index is on. The given index is with respect to the
        original collection item. Recall that the pagination pages are zero based.
        
        Return page number, or -1 for out of range indices
        """
        if item_index >= self.items or item_index < 0 or not self.paginated:
            return -1
                            
        return item_index // self.items_per_page

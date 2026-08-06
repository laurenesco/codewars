# https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python

class Block:
    def __init__(self, dimensions: tuple[float, float, float]) -> None:
        """
        Initialize Block object with provided dimensions
        """
        
        if len(dimensions) != 3:
            raise ValueError(f"Expected 3 dimensions, got {len(dimensions)}")
        
        self.width, self.length, self.height = dimensions
        
    def get_width(self) -> float:
        """
        Return Block width
        """
        return self.width
    
    def get_length(self) -> float:
        """
        Return Block length
        """
        return self.length
    
    def get_height(self) -> float:
        """
        Return Block height
        """
        return self.height
    
    def get_volume(self) -> float:
        """
        Return Block volume
        """
        return self.length * self.width * self.height
    
    def get_surface_area(self) -> float:
        """
        Return surface area of Block
        """
        return 2 * (self.length * self.height) + 2 * (self.width * self.height) + 2 * (self.length * self.width)

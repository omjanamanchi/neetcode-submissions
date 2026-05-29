class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, t1, t2=None):
        if t2 is None:
            format_text = t1.upper()
            return format_text
        else:
            format_text = t1 + t2
            return format_text




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    # tag = "html"

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content is not None:
            self.append(content)

    def append(self, new_content):
        if not new_content:
            raise ValueError("cannot append nothing")
        if isinstance(new_content, str):
            new_content = StringWrapper(new_content)
        self.content.append(new_content)

    # def render(self, out_file):
    #     # <html> this is the content </html>
    #     out_file.write(f"<{self.tag}>\n")

    #     print(self.content)
    #     for cont in self.content:
    #         try:
    #             cont.render(out_file)
    #         except AttributeError:
    #             out_file.write(cont)
    #         out_file.write('\n')

    #     out_file.write(f"</{self.tag}>")

    def render(self, out_file):
        # <html> this is the content </html>
        out_file.write(f"<{self.tag}>\n")

        for cont in self.content:
            cont.render(out_file)
            out_file.write('\n')

        out_file.write(f"</{self.tag}>")


class StringWrapper(str):
    def render(self, out_file):
        out_file.write(self)


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write(f"<{self.tag}>")
        self.content[0].render(out_file)
        out_file.write(f"</{self.tag}>")

    def append(self, new_content):
        if len(self.content) > 0:
            raise TypeError("cannot append to a OneLineTag")
        super().append(new_content)


class Title(OneLineTag):
    tag = "title"






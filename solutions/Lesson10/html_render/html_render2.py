#!/usr/bin/env python3

"""
Solution without a TextWrapper
"""


class Element:

    # subclasses should set an actual tag
    tag = "placeholder"  # jsut so there is something
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = []
        if content:
            # call the class's append method
            # so that it can do anything special it needs to do
            self.append(content)

    def append(self, content):
        """
        add a new piece of content or another element to this element
        """
        self.contents.append(content)

    def _make_tags(self):
        """
        create the tags
        -- in a separate method so different subclass' render methods can use it
        """
        attrs = " ".join(f'{key}="{val}"' for key, val in self.attributes.items())
        open_tag = f"<{self.tag} {attrs}".strip() + ">"

        close_tag = f"</{self.tag}>"

        return open_tag, close_tag

    def render(self, out_file, cur_ind=""):

        open_tag, close_tag = self._make_tags()

        out_file.write(cur_ind + open_tag + "\n")
        for stuff in self.contents:
            try:
                stuff.render(out_file, cur_ind + self.indent)
            except AttributeError:  # assume it's a string
                out_file.write(cur_ind + self.indent + stuff)
        out_file.write("\n" + cur_ind + close_tag)


class OneLineTag(Element):

    def append(self, content):
        if self.contents:
            raise TypeError("OneLineTag elements can not have content added")
        else:
            super().append(content)

    def render(self, out_file, cur_ind=""):
        open_tag, close_tag = self._make_tags()
        # oddly, writelines doesn't add a newline
        # so it's really "write sequence"
        out_file.writelines((cur_ind,
                             open_tag,
                             self.contents[0],
                             close_tag))


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(file_out, cur_ind=cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    """
    base class for tags that have no content
    """

    def append(self, *args, **kwargs):
        """
        self closing tags can't have content, so we raise an error if someone
        tries to add some.
        """
        raise TypeError("You can not add content to a self closing tag")

    def render(self, out_file, ind=""):
        # there is some repetition here -- maybe factor that out?
        open_tag, _ = self._make_tags()
        # make it a self closing tag by adding the /
        out_file.write(ind + open_tag.replace(">", " />"))


class Hr(SelfClosingTag):
    """
    Horizontal Rule
    """
    tag = "hr"


class Br(SelfClosingTag):
    """
    Line break
    """
    tag = "br"


class A(OneLineTag):
    """
    anchor element
    """
    tag = "a"

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
#        super(A, self).__init__(content, **kwargs)
        # OneLineTag.__init__(self, *args, **kwargs)
        #super().__init__(*args, **kwargs)
        # this could also be direct:
        Element.__init__(self, *args, **kwargs)


class Ul(Element):
    """
    unordered list
    """
    tag = "ul"


class Li(Element):
    """
    list element
    """
    tag = "li"


class H(OneLineTag):
    """
    section head
    """
    tag = "H"

    def __init__(self, level, *args, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(*args, **kwargs)


class Meta(SelfClosingTag):
    """
    metadata tag
    """
    tag = "meta"

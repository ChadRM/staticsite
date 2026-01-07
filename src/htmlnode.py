"""Classes for representing and rendering HTML nodes.

This module provides classes to represent HTML nodes, including both
leaf nodes and parent nodes. It contains functionality to specify
HTML tags, attributes, content, or child elements and to convert these
representations to HTML string format.
"""


class HTMLNode():
    """
    Represents a node in an HTML document.

    This class is used to model HTML elements, including their tags, values,
    child elements, and properties. It provides a basic framework to support
    the construction and representation of an HTML document by encapsulating
    the structural and attribute-related details of an HTML element.

    :ivar tag: The HTML tag associated with this node (e.g., 'div', 'p').
    :type tag: str or None
    :ivar value: The textual content or value enclosed by this node.
    :type value: str or None
    :ivar children: A collection of child nodes nested under this node.
    :type children: list[HTMLNode] or None
    :ivar props: A dictionary of HTML attributes and their respective values
        for this node (e.g., {'id': 'content', 'class': 'main'}).
    :type props: dict[str, str] or None
    """
    def __init__(self,tag=None,value=None,children=None,props=None):
        """
        Initializes a new instance of a class with the provided tag, value, children,
        and props attributes.

        :param tag: Represents the tag attribute for the object.
        :type tag: Optional[Any]
        :param value: Represents the value associated with the object.
        :type value: Optional[Any]
        :param children: Represents the list or structure defining child elements.
        :type children: Optional[Any]
        :param props: Represents additional properties or metadata for the object.
        :type props: Optional[Any]
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        """
        Converts the properties stored in a dictionary to an HTML attributes string format. If
        no properties are available, an empty string is returned. Each key-value pair in the
        dictionary is formatted as key="value" and concatenated into a string.

        :raises AttributeError: If `self.props` is not defined.
        :raises TypeError: If `self.props` is not a dictionary.
        :return: A string with concatenated HTML attributes derived from the dictionary
            ``self.props``. Returns an empty string if the dictionary is ``None``.
        :rtype: str
        """
        if self.props is None:
            return ""
        output = " "
        for key,value in self.props.items():
            output += key + "=\"" + value + "\" "
        return output

    def __repr__(self):
        """
        Provides a string representation of the object suitable for debugging.

        This method returns a formatted string that contains details about the object's
        relevant attributes.

        :return: A string representing the object's state, including its tag, value,
            children, and props.
        :rtype: str
        """
        return f"(HTML NODE:tag={self.tag},value={self.value},children={self.children},props={self.props})"


class LeafNode(HTMLNode):
    """
    Represents a leaf node in an HTML tree.

    A leaf node is a terminal node that cannot have children nodes. It contains
    a tag and a value, and optionally, properties associated with the tag.

    :ivar tag: HTML tag of the node.
    :type tag: str
    :ivar value: Content or inner text of the HTML tag.
    :type value: str
    :ivar props: Optional attributes or properties of the HTML tag.
    :type props: dict
    """
    def __init__(self, tag, value, props={}):
        """
        Initializes a new instance of the class with the specified tag, value, and properties.

        This constructor is used to create and initialize an object with a specific tag,
        value, and optional properties. The `tag` parameter determines the kind of object
        being created, while `value` stores the primary data or content associated with
        the object. Additional attributes or metadata can be passed through the `props`
        dictionary.

        :param tag: The tag that identifies the type or categorization of the object.
            It is a required parameter.
        :param value: The primary content or data to be stored in the object.
            It is a required parameter.
        :param props: An optional dictionary containing key-value pairs of additional
            properties or metadata associated with the object. Defaults to an empty dictionary.
        """
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        """
        Converts the contents of a node into an HTML string representation.

        This method generates an HTML string based on the tag and value of the
        current node. If the tag is not specified, it simply returns the value.

        :raises ValueError: If the value is missing or empty.
        :return: A string containing the HTML representation of the node.
        """
        if self.value is None or self.value == "":
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    """
    Represents an HTML parent node with a specific tag and child nodes.

    This class is an extension of the HTMLNode class and is designed to represent
    an HTML element that must have a tag and children. The `to_html` method
    generates the HTML representation of the parent node including its children.

    :ivar tag: The HTML tag associated with the node.
    :type tag: str
    :ivar children: The child nodes of this parent node. Must not be empty.
    :type children: list[HTMLNode]
    :ivar props: The attributes or properties applied to this node, represented as
        a dictionary. Defaults to an empty dictionary.
    :type props: dict
    """
    def __init__(self, tag, children, props={}):
        """
        Initializes an instance of the class representing a hierarchical node structure.

        The instance represents a node with a specific tag, a collection of child nodes,
        and additional properties. This structure allows the representation of tree-like
        hierarchical data or document object models.

        :param tag: The identifier for the node, typically used as its type or name.
        :type tag: str

        :param children: The list of child nodes associated with this node.
        :type children: list

        :param props: A dictionary of additional properties or attributes associated
                      with this node that define its behavior or metadata. It defaults
                      to an empty dictionary if not provided.
        :type props: dict
        """
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        """
        Converts a structured representation of an HTML element and its children
        into an HTML string. This function assumes that the class instance has
        certain properties indicating the tag and children elements.

        :param self: Represents the instance of the class containing this method.
        :return: A string representing the HTML representation of the given element
            and its children.
        :rtype: str
        :raises ValueError: If no tag is provided or if there are no child elements.
        """
        if self.tag is None or self.tag == "":
            raise ValueError("parents must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("parents must have children")
        output = f"<{self.tag}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"
        return output
     

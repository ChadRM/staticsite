from textnode import TextNode, TextType

def main():
    textnode = TextNode("Some Text",TextType.LINK,"http://yourmom.com")
    print(textnode)



if __name__ == "__main__":
    main()
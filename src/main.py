from textnode import TextNode, TextType

def main():
    text_node = TextNode("Some Text", TextType.LINK, "https://yourmom.com")
    print(text_node)



if __name__ == "__main__":
    main()
#jb try chalega tb bhi finally chalega aur agr try nahi chala tb bhi finally chalega. finally ka use ffunctions mein krenge.
def main():
    try:
        a = int(input("Enter the number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("ji haan")

main()
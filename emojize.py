import emoji
def main():
     response = emoji.emojize("hello world, :earth_africa:")
     

     '''for r in response:
      if r == ",":
          words, emoji = response.split(",")
          e = emoji.emojize(emoji[-1])
          print(words + e)'''
     
     print(emoji.emojize(response))

if __name__ == "__main__":
    main()


                         
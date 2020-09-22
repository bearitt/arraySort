from sortCharacter import sortCharacterList
from sortInteger import sortIntegerList
from sortString import sortStringList

def main():
    charList = ['F','A','d','c','1','@'];
    intList = [7,-1,-4,2,5,-5];
    stringList = ['Demi','Francis','Eobard','Albert','Christina','Brian']
    print("Character list is:"+ str(charList))
    print("Integer list is:"+ str(intList))
    print("String list is:" + str(stringList))
    print("")
    print("Sorting each one of them is as follows:")
    print("Sorted Character list"+ str(sortCharacterList(charList)))
    print("Sorted Integer list"+ str(sortIntegerList(intList)))
    print("Sorted String list"+ str(sortStringList(stringList)))


if __name__ == '__main__':
    main()
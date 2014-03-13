'''
Created on Mar 12, 2014

@author: marphill
'''

def fizz_buzz(end=100):
    """ Purpose is to print out all numbers between 1 and 100 (or to the end specified). 
        For each number that is divisible by three, print "Fizz"; for each number 
        divisible by five print "Buzz". If a number is divisible by both 3 and 5, print
        "FizzBuzz". Each number should print to a new line.
        
        Answers can be found for a good variety of languages at http://c2.com/cgi/wiki?FizzBuzzTest
    """
    count = 0
    while count <= 100:
        output = ""
        if count % 3 == 0:
            output += "Fizz"
        if count % 5 == 0:
            output += "Buzz"
        if output != "":
            print output
        else:
            print count
        count += 1
        
def fizz_buzz_test(tester=3):
    """ Tests the FizzBuzz Algorithm. Simply copy and paste code in here.
        Set the number and make sure you are getting correct values.
    """
    output = ""
    if tester % 3 == 0:
        output += "Fizz"
    if tester % 5 == 0:
        output += "Buzz"
    if output != "":
        return output
    else:
        return tester
    
def nameformatter(name):
    """ See the highlighted Java code below for more context to this function.
    """
    if not name: return None if name is None else "" # Return empty and None case
    mixed = False; lower = False; upper = False; beginspaces = True; endspaces = True;
    mod_case = []; original_case = []
    for c in range(0, len(name)):
        if name[c] == " ": # Handle spaces
            if beginspaces or endspaces:
                continue
            endspaces = True
            continue
        elif beginspaces:
            beginspaces = False
        if endspaces:
            endspaces = False
            if len(original_case) != 0:
                if not mixed: mod_case.append(" ")
                original_case.append(" ")
        if not mixed:
            if (lower and name[c].isupper()) or (upper and name[c].islower()):
                mixed = True
                original_case.append(name[c])
                continue
            elif not upper and name[c].isupper():
                upper = True
            elif not lower and name[c].islower():
                lower = True
            if len(mod_case) == 0 or mod_case[len(mod_case)-1] == " ":
                mod_case.append(name[c].upper())
            else:
                mod_case.append(name[c].lower())     
        original_case.append(name[c])
    if mixed:
        return "".join(original_case)
    else:
        return "".join(mod_case)
    
"""
This was a test given to me in Java. It is so much easier to do this in Python,
but I wanted to add this in here to see how I did this in Java. This 
gives context to the NameFormatter that I worked on.
public class NameFormatter2 {
    
    /**
     * Convert a name string to a beautified output.  This basically cleans
     * out extra whitespace from the name string, and converts it to proper case.
     * If the name is already mixed case, it's assumed that is on purpose, so this
     * method will not convert the capitalization, but still clean up extra whitespace.
     * 
     * Requirements:
     * - if the input is null, return null
     * - if the input is a 0-length string, return an empty string
     * - if the input is mixed case (contains upper and lower case), trim out extra spaces
     * - if the input is all upper case or all lower case, capitalize first letter of each word, lower case other letters, and trim out extra spaces
     * 
     * Useful Java calls:
     * 
     * String class:
     * - input.toUpperCase()
     * - input.toLowerCase() 
     * - input.trim() 
     * - input.split(String separator)
     * - input.toCharArray()
     * 
     * - Character.toUpperCase(char c)
     * - Character.toLowerCase(char c)
     * - Character.isUpperCase(char c)
     * - Character.isLowerCase(char c)
     * 
     * @param input the name string to be formatted
     * @return a formatted version of the string, null if the input is null
     */
    public static String formatNameString(String input) {
        //This one was a combination of a few others work. Mine is in
        //formatNameStringOriginal
      
      
        //********************************************************************************
        
        /*
         * Implement the requirements of this method here.  Use the main method provided to
         * run this class and verify the proper functionality of this method.
         */
         
        //********************************************************************************
        String toReturn = "";
        for (String word :(input == null) ? "".split(" ") : input.split(" ")) toReturn += (word.length()>0?(input.equals(input.toLowerCase()) || input.equals(input.toUpperCase())?Character.toUpperCase(word.charAt(0)) + word.substring(1).toLowerCase():word)+" ":"");
        return (input == null) ? null : toReturn.trim();
        
    }
    
    public static String formatNameStringOriginal(String input) {
        // This was my original work.
      
        //********************************************************************************
        
        /*
         * Implement the requirements of this method here.  Use the main method provided to
         * run this class and verify the proper functionality of this method.
         */
         
        //********************************************************************************
        if(input == null){
            return null;
        } else if(input.length() == 0){
            return "";
        } else{
            input = input.trim();
            
            String[] names = input.split(" "); //Split on the spaces in between to test each word for casing individually

            if (names.length == 1 && input.length() == 1){
                return input.toUpperCase(); //Return single character case
            }
            int is_case = 0; //0 for upper, 1 for lower, 2 for mixed
            char[] chars = input.toCharArray();
            //Check for upper, lower, mixed case, incorrect casing
            for (int i = 0; i < chars.length; i++){
                if(Character.isUpperCase(chars[i]) && is_case == 1) {
                    is_case = 2;
                    break; //Break out of for loop with mixed case input
                } else if(Character.isLowerCase(chars[i])){
                    is_case = 1;
                }
                //If character was uppercase, do nothing (will return 0 if all are uppercase)
            }
            input = "";
            if(is_case == 0 || is_case == 1){
                for(int j=0; j < names.length; j++){
                    chars = names[j].toCharArray();
                    for(int k = 0; k < chars.length; k++){
                        if(k == 0){
                            chars[k] = Character.toUpperCase(chars[k]);
                        } else{
                            chars[k] = Character.toLowerCase(chars[k]);
                        }
                    }
                    if(j==0){
                        input += new String(chars);
                    } else{
                        if (!names[j].isEmpty()){
                            input +=  " " + new String(chars);
                        }                            
                    }
                }
            }
            if(is_case == 2){
                for(int j=0; j < names.length; j++){
                    if(j==0){
                        input += new String(names[j]);
                    } else{
                        if (!names[j].isEmpty()){
                            input += " " + new String(names[j]);
                        }
                    }
                }
            }
// System.out.println("input final:" + input);
        }
         
        return input;
        
    }
    
    
    // TEST CASES BELOW
    
    /**
     * Test the formatNameString method and report the success/failure.
     */
    public static int test(String input, String expected) {
        String output = formatNameString(input);
        if (expected == null && output == null) {
            System.out.println("SUCCESS: ["+input+"] => ["+output+"]");
            return 0;
        } else if (expected == null && output != null) {
            // error
        } else if (!expected.equals(output)) {
            // error
        } else {
            System.out.println("SUCCESS: ["+input+"] => ["+output+"]");
            return 0;
        }
        System.out.println("ERROR:   ["+input+"] => ["+output+"] *** SHOULD BE ["+expected+"]");
        return 1;
    }
    
    public static void main(String[] args) {
        int errors = 0;
        
        // test null input
        errors += test(null, null);
        
        // test empty input
        errors += test("", "");
        
        // test single character input
        errors += test("A", "A");
        errors += test("b", "B");
        
        // test single name input
        errors += test("bob", "Bob");
        errors += test("BOB", "Bob");
        errors += test("McDonald", "McDonald");
        
        // test multiple character input
        errors += test("a b", "A B");
        errors += test("A B", "A B");
        
        // test multiple name input
        errors += test("jim jones", "Jim Jones");
        errors += test("JOHN JOE DOE", "John Joe Doe");
        errors += test("Mike McRae", "Mike McRae");
        errors += test("mike McRae", "mike McRae");

        // test trimming extra whitespace
        errors += test("  jim  jones", "Jim Jones");
        errors += test("JOHN   JOE DOE", "John Joe Doe");
        errors += test("Mike McRae  ", "Mike McRae");
        errors += test(" mike  McRae ", "mike McRae");
        
        System.out.println();
        if (errors > 0) System.out.println("There were "+errors+" error(s).");
        else System.out.println("All tests pass.");
    }
}
"""
def test(test, expected):
    """Helper method to test nameformatter"""
    result = nameformatter(test)
    if  result == expected:
        print "Success: {} = {}".format(result, expected)
        return 0
    else:
        print "Failure: {} != {}".format(result, expected)
        return 1

if __name__ == '__main__':
    print fizz_buzz_test(1) == 1 # True
    print fizz_buzz_test(3) == 3 # False
    print fizz_buzz_test(5) == 5 # False
    print fizz_buzz_test(3) == "Fizz" # True
    print fizz_buzz_test(6) == "Fizz" # True
    print fizz_buzz_test(9) == "Fizz" # True
    print fizz_buzz_test(12) == "Fizz" # True
    print fizz_buzz_test(18) == "Fizz" # True
    print fizz_buzz_test(21) == "Fizz" # True
    print fizz_buzz_test(5) == "Buzz" # True
    print fizz_buzz_test(10) == "Buzz" # True
    print fizz_buzz_test(15) == "FizzBuzz" # True
    print fizz_buzz_test(20) == "Buzz" # True
    print fizz_buzz_test(25) == "Buzz" # True
    print fizz_buzz_test(30) == "FizzBuzz" # True
    print
    print "------------------- NameFormatterTest ---------------------"
    print nameformatter("Hi There")
    print len(nameformatter("Hi There"))
    print nameformatter("Hi There") == "Hi There"
    errors = 0;
         
    errors += test(None, None);
     
    # test empty input
    errors += test("", "");
     
    # test single character input
    errors += test("A", "A");
    errors += test("b", "B");
     
    # test single name input
    errors += test("bob", "Bob");
    errors += test("BOB", "Bob");
    errors += test("McDonald", "McDonald");
     
    # test multiple character input
    errors += test("a b", "A B");
    errors += test("A B", "A B");
     
    # test multiple name input
    errors += test("jim jones", "Jim Jones");
    errors += test("JOHN JOE DOE", "John Joe Doe");
    errors += test("Mike McRae", "Mike McRae");
    errors += test("mike McRae", "mike McRae");
 
    # test trimming extra whitespace
    errors += test("  jim  jones", "Jim Jones");
    errors += test("JOHN   JOE DOE", "John Joe Doe");
    errors += test("Mike McRae  ", "Mike McRae");
    errors += test(" mike  McRae ", "mike McRae");
    
    # test weird characters
    errors += test(" 32$5% John ", "32$5% John")
    errors += test("#$1~", "#$1~")
    errors += test("12345P", "12345p")
     
    print
    if errors > 0: print "There were "+str(errors)+" error(s)."
    else: print "All tests pass."

    
    
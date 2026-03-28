#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

/**
 * Checks if a string is a palindrome.
 * Ignores case and non-alphanumeric characters.
 */
bool is_palindrome(const char *text) {
    int left = 0;
    int right = strlen(text) - 1;

    while (left < right) {
        // Skip non-alphanumeric characters from the left
        if (!isalnum(text[left])) {
            left++;
        } 
        // Skip non-alphanumeric characters from the right
        else if (!isalnum(text[right])) {
            right--;
        } 
        // Compare characters (case-insensitive)
        else {
            if (tolower(text[left]) != tolower(text[right])) {
                return false;
            }
            left++;
            right--;
        }
    }
    return true;
}

int main() {
    const char *test_str = "Race a car?"; // Change this to test!
    
    if (is_palindrome(test_str)) {
        printf("'%s' is a palindrome.\n", test_str);
    } else {
        printf("'%s' is NOT a palindrome.\n", test_str);
    }

    return 0;
}

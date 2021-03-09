#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum tbool tbool;
enum tbool{
    FALSE=0,
    TRUE=1,
};

tbool EstPalindrome(char *phrase){
    int n=strlen(phrase);
    int i=0;
    while (i<n/2){
        if (phrase[i]!=phrase[n-i-1]){
            return FALSE;
        }
        i++;
    }
    return TRUE;
}

int main(){
    tbool test = EstPalindrome("BLYAT");
    printf("Est-ce un palindrome %s\n", test? "Oui" : "Non");
}
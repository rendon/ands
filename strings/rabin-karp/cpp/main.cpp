// Reference: Algorithms 4th Ed., Robert Sedgewick, Kevin Wayne

#include <bits/stdc++.h>
using namespace std;
typedef long long int64;

class RabinKarp {
private:
    int64 const Q = 1000000007; // A large prime number
    int64 const R = 256; // Alphabet size

    int64 hash(string const& str, int len) const {
        int64 h = 0;
        for (int i = 0; i < len; i++) {
            h = (h * R + str[i]) % Q;
        }
        return h;
    }

    bool match(string const& text, string const& pattern, int start) {
        for (int i = 0; i < pattern.size(); i++) {
            if (text[start+i] != pattern[i]) {
                return false;
            }
        }
        return true;
    }
public:
    int search(string text, string pattern) {
        int n = text.size();
        int m = pattern.size();

        if (n < m) { return -1; }

        int64 RM; // Will store R^(m-1)
        // Compute R^(m-1)
        RM = 1;
        for (int i = 1; i < m; i++) { RM = (RM * R) % Q; }

        int64 patHash = hash(pattern, m);
        int64 textHash = hash(text, m);
        if (patHash == textHash && match(text, pattern, 0)) {
            return 0;
        }

        for (int i = m; i < n; i++) {
            textHash = (textHash + Q - (RM * text[i-m]) % Q) % Q; // Remove leading character
            textHash = (textHash * R + text[i]) % Q;              // Add trailing character
            if (patHash == textHash && match(text, pattern, i - m + 1)) {
                return i - m + 1;
            }
        }
        return -1;
    }
};

int main() {
    auto rk = RabinKarp();
    assert(rk.search("abc", "") == 0);
    assert(rk.search("", "") == 0);
    assert(rk.search("ab", "abcd") == -1);
    assert(rk.search("hello world", "hello") == 0);
    assert(rk.search("hello world", "world") == 6);
    return 0;
}

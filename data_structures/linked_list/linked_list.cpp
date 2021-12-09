#include <iostream>
using namespace std;


class Link {
    private:
        // Because I didn't know the 'this' prefix was the way to show that you
        // were access class variables when I started, all vars starting with
        // a '_' are private class variables.
        // Were I to redo this, these would all simply be "*next", etc. Then,
        // when I accessed them later, it'd be with "this.next", etc.
        Link *_next = NULL;
        Link *_previous = NULL;
        string _data;
        int _index;

    public :
        // Get the next link in the chain
        Link* next() {
            return _next;
        }

        // Get the previous link in the chain
        Link* previous() {
            return _previous;
        }

        // Set the next link in the chain.
        void set_next(Link *next) {
            _next = next;
        }

        // Set the previous link in the chain
        void set_previous(Link *previous) {
            _previous = previous;
        }

        // Give this link some sort of data
        void set_data(string data) {
            _data = data;
        }

        // return the data. Thinking about it, the data variable should probably
        // be a public variable, but oh well.
        string data() {
            return _data;
        }

        // Print out the data that this class has oh-so prettily
        void print() {
            cout << _data << endl;
        }
};


class LinkedList {
    private:
        Link *_head = NULL;
        Link *_end = NULL;
        Link *_current = NULL;
        int _length = 0;

    public:
        // Adds a new linked list
        void add(Link *next) {
            // Check if the pointer has been initialized or not
            if (_head == NULL) {
                // initialize this with all elements being the element passed in
                _head = next;
                _end = next;
                _current = next;
            }
            else {
                // Play musical chairs to get the list linked properly
                // Originally looks like this
                // [end] <- [next]
                // As can be seen, [next] is going to become the new [end].
                // That means we have to place [next]'s pointer as the pointer
                // for [end]'s *next.
                // Then we set [next] to be the new [end] of the linked list.
                next->set_previous(_end);
                _end->set_next(next);
                _end = next;
            }
            _length += 1;
        }

        // Returns the length. I really wanted this to be a lambda function
        // that calculates the length when you access it, but I couldn't figure
        // that part out yet.
        int get_length() {
            return _length;
        }

        // Returns the current list element
        Link* get_current() {
            return _current;
        }

        // Returns the end of the list
        Link* get_end() {
            return _end;
        }

        // Returns the head of the list.
        Link* get_head() {
            return _head;
        }

        // Sets the current element to be the next element.
        // Returns the new current element.
        Link* next() {
            _current = _current->next();
            return _current;
        }

        // Sets the current element to be the previous element.
        // Returns the new previous element.
        Link* previous() {
            _current = _current->previous();
            return _current;
        }

        // Sets the current link to the link passed in.
        void set_current(Link* current) {
            _current = current;
        }

};



int main() {
    // I'm going to use the alphabet as my data
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    // initialize a new linked list
    LinkedList L = LinkedList();

    string val;
    for (int i = 0; i<alphabet.length(); i++) {
        // Note the 'new' keyword. This IS required if you want to make more
        // than a single link. Without this, only a single link is created, and
        // all data inside it gets overwritten.
        Link *item = new Link;
        // If you DON'T cast this to a string, everything fucks up.
        string charval(1, alphabet[i]);
        val = "This is item " + charval;

        // Set the value of this link.
        item->set_data(val);
        // Add that link to the list.
        L.add(item);
    }


    // Check the length of the list. It should be 26.
    cout << L.get_length() << endl;

    // Test running through it forwards.
    while (! L.get_current() == NULL) {
        L.get_current()->print();
        L.next();
    }

    // Bring the current one back one.
    L.set_current(L.get_end());

    // Test running through the list backwards too.
    while (! L.get_current() == NULL) {
        L.get_current()->print();
        L.previous();
    }

    return 0;
}

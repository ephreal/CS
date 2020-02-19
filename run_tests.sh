# Runs all tests. Currently only supports python tests.

echo ""
echo "Python tests:"
python -m unittest discover tests/python

echo ""
echo "Ruby tests:"
RUBY_FILES=$(ls tests/ruby)

for ruby_file in $RUBY_FILES; do
ruby "tests/ruby/$ruby_file"
done

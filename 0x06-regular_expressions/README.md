# Regular Expressions (REGEXP) and Oniguruma Ruby Library

## Table of Contents
- [Introduction to Regular Expressions](#introduction-to-regular-expressions)
- [Oniguruma Ruby Library](#oniguruma-ruby-library)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Regular Expression Syntax](#regular-expression-syntax)
- [Commonly Used Patterns](#commonly-used-patterns)
- [Additional Resources](#additional-resources)

## Introduction to Regular Expressions

Regular expressions, often abbreviated as REGEXP, are powerful tools used for pattern matching and text manipulation. They provide a concise and flexible way to search, match, and manipulate strings based on specific patterns.

A regular expression consists of a sequence of characters that define a search pattern. It can include a combination of literals, metacharacters, and special sequences. The pattern is used to match against input strings, allowing you to perform operations such as finding matches, replacing text, or extracting specific information from a string.

Regular expressions are supported by many programming languages and tools, including Ruby. They are widely used in various domains, such as data validation, text processing, parsing, and web scraping.

## Oniguruma Ruby Library

Oniguruma is a regular expression library that originated in Japan. It provides powerful regular expression matching and manipulation capabilities for various programming languages, including Ruby. Oniguruma is known for its rich set of features, high performance, and support for a wide range of regular expression syntaxes.

### Installation

To use the Oniguruma Ruby library, you need to ensure that it is installed on your system. Follow the steps below to install it:

1. **Prerequisites**: Make sure you have Ruby installed on your system.

2. **Gem Installation**: Open your terminal and run the following command to install the Oniguruma gem:

   ````
   gem install oniguruma
   ```

   This command will download and install the Oniguruma gem from the RubyGems repository.

3. **Verify Installation**: To verify that Oniguruma is installed correctly, run the following command:

   ````
   ruby -e "require 'onigmo'; puts Oniguruma::VERSION"
   ```

   If Oniguruma is installed correctly, you will see the version number printed in the terminal.

### Basic Usage

To use the Oniguruma Ruby library in your code, you need to require it first:

```ruby
require 'oniguruma'
```

Once you have required the library, you can create an instance of the `Oniguruma::ORegexp` class, which represents a compiled regular expression:

```ruby
regex = Oniguruma::ORegexp.new('pattern')
```

You can then use various methods provided by the `ORegexp` class to perform operations such as matching, replacing, or extracting information from strings.

Here's an example that demonstrates how to use Oniguruma to match a pattern in a string:

```ruby
require 'oniguruma'

# Create a regular expression object
regex = Oniguruma::ORegexp.new('world')

# Match the regular expression against a string
result = regex.match('Hello, world!')

# Print the matched substring
puts result[0] # Output: "world"
```

This is just a simple example, and Oniguruma provides many more advanced features and methods for working with regular expressions.

### Regular Expression Syntax

Oniguruma Ruby library supports a rich set of regular expression syntaxes. The syntax is similar to other common regular expression flavors, such as Perl-compatible regular expressions (PCRE).

For detailed information about the regular expression syntax supported by Oniguruma, you can refer to the official documentation:

- [Oniguruma Syntax Documentation](https://github.com/k-takata/Onigmo/blob/master/doc/RE)

The documentation provides comprehensive information about metacharacters, character classes, quantifiers, anchors, and other elements of the regular expression syntax.

### Commonly Used Patterns

Here are some commonly used patterns and examples that can be achieved using the Oniguruma Ruby library:

- **Matching a specific word**: To match a specific word in a string, you can use the word boundary `\b` anchor:

  ````ruby
  regex = Oniguruma::ORegexp.new('\bworld\b')
  result = regex.match('Hello, world!')
  puts result[0] # Output: "world"
  ```

- **Matching digits**: To match one or more digits in a string, you can use the `\d` metacharacter:

  ````ruby
  regex = Oniguruma::ORegexp.new('\d+')
  result = regex.match('The answer is 42')
  puts result[0] # Output: "42"
  ```

- **Matching email addresses**:```ruby
  regex = Oniguruma::ORegexp.new('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
  result = regex.match('Email me at john@example.com')
  puts result[0] # Output: "john@example.com"
  ```

- **Replacing text**: To replace occurrences of a pattern in a string, you can use the `sub` or `gsub` methods:

  ````ruby
  regex = Oniguruma::ORegexp.new('world')
  text = 'Hello, world!'
  replaced_text = regex.gsub(text, 'Ruby')
  puts replaced_text # Output: "Hello, Ruby!"
  ```

- **Extracting information**: To extract specific information from a string using capturing groups, you can use the `[]` method:

  ````ruby
  regex = Oniguruma::ORegexp.new('(\d{2})-(\d{2})-(\d{4})')
  result = regex.match('Date: 01-03-2024')
  puts result[1] # Output: "01"
  puts result[2] # Output: "03"
  puts result[3] # Output: "2024"
  ```

These are just a few examples to give you an idea of what you can achieve with regular expressions using the Oniguruma Ruby library. The possibilities are vast and depend on your specific use case.

###Regular Expression Features:

Regular expressions provide a wide range of features to express complex patterns. Some common features include:

- Metacharacters: Metacharacters are special characters with a predefined meaning in regular expressions. For example, . matches any character, * matches zero or more occurrences, and + matches one or more occurrences.
- Character Classes: Character classes allow you to specify a set of characters to match. For example, [abc] matches either 'a', 'b', or 'c'. You can also use predefined character classes like \d for digits, \w for word characters, and \s for whitespace characters.
- Quantifiers: Quantifiers specify the number of occurrences to match. For example, ? matches zero or one occurrence, {n} matches exactly n occurrences, and {n,} matches n or more occurrences.
- Anchors: Anchors are used to match positions within a string. The ^ anchor matches the start of a line, while the $ anchor matches the end of a line.
- Grouping and Capturing: Parentheses are used to group parts of a pattern together. They also allow you to capture the matched substring for later use. For example, (\d{2})-(\d{2})-(\d{4}) captures the day, month, and year in a date pattern.

### Additional Resources

Here are some additional resources to learn more about regular expressions and the Oniguruma Ruby library:

- [Ruby Documentation on Regular Expressions](https://ruby-doc.org/core-3.0.0/Regexp.html): Official Ruby documentation on regular expressions.
- [Oniguruma GitHub Repository](https://github.com/k-takata/Onigmo): The official GitHub repository for Oniguruma with documentation and examples.
- [Rubular](https://rubular.com/): An online tool to test and experiment with Ruby regular expressions.
- [Regular-Expressions.info](https://www.regular-expressions.info/): A comprehensive website with tutorials, examples, and resources about regular expressions.



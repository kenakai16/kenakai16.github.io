---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Notebooks with MyST Markdown

## Number Theory
What are numbers? I promise to not be too philosophical in this book, but are numbers not a construct we have defined? Why do we have the digits 0 through 9, and not have more digits than that? Why do we have fractions and decimals and not just whole numbers? This area of math where we muse about numbers and why we designed them a certain way is known as number theory.
Number theory goes all the way back to ancient times, where mathematicians study different number systems and why we have accepted them the way we do today. Here are different number systems that you may recognize:
### Natural Numbers
These are the numbers 1, 2, 3, 4, 5... and so on. Only positive numbers are included here, and are the earliest known system. Natural numbers are so ancient cavemen scratched tally marks on bones and cave walls to keep records.

### Whole Numbers
Adding to natural numbers, the concept of “0” was later accepted and we call these “whole numbers.” The Babylonians also developed the useful idea for place-holding notation for empty “columns” on numbers greater than 9, such as “10”, “1000”, or “1090.” Those zeros indicate no value occupying that column.
THIS IS NOT A FULL MATH CRASH COURSE!
This is by no means a comprehensive review of high school and college math. If you want that, a great book to check out is No Bullshit Guide to Math and Physics by Ivan Savov. The first few chapters contain the best crash course on high school and college math I have ever seen. The book Mathematics 1001 by Dr. Richard Elwes has some great content as well, and in bite-sized explanations.

### Integers
Integers include positive and negative whole numbers as well as 0. We may take them for granted, but ancient mathematicians were deeply distrusting of the idea of negative numbers. But when you subtract 5 from 3, you get -2. This is useful especially when it comes to finances where we measure profits and losses. In 628 AD, an Indian mathematician named Brahmagupta showed why negative numbers were necessary for arithmetic to progress, and therefore integers became accepted.

### Rational Numbers
Any number that you can express as a fraction, such as , is a rational
number. This includes all finite decimals and integers since they can be expressed as fractions too, such as and respectively.
They are called rational because they are ratios. Rational numbers were quickly deemed necessary bececause because time, resources, and other quantities could not always be measured in discrete units. Milk does not always come in gallons. We may have to measure it as parts of a gallon. If I run for 12 minutes, I cannot be forced to measure in whole miles when in actuality I ran of a mile.

### Irrational Numbers
Irrational numbers cannot be expressed as a fraction. This includes the famous Pi , square roots of certain numbers like , and Euler’s number which we will learn about later. These numbers have an infinite number of decimal digits, such as

$$
\Pi = 3.14159265359
$$

There is an interesting history behind irrational numbers. The Greek mathematician Pythagoras believed all numbers are rational. He believed this so fervently, he made a religion that prayed to the number 10. "Bless us, divine number, thou who generated gods and men!" he and his followers would pray (why “10” was so special, I do not know).

### Real Numbers
Real numbers include rational as well as irrational numbers. In practicality, when you are doing any data science work you can treat any decimals you work with as real numbers.

### Complex and Imaginary Numbers
You encounter this number type when you take the square root of a negative number. While imaginary and complex numbers have relevance in certain types of problems, we will mostly steer clear from them for our purposes


## Order of Operations
Hopefully you are familiar with order of operations which is the order you solve each part of a mathematical expression. As a brief refresher, recall you evaluate components in parantheses, followed by exponents, then multiplication, division, addition, and subtraction. You can remember the
order of operations by the mnemonic device PEMDAS (Please Excuse My Dear Aunt Sally) which corresponds to the ordering paranthesis, exponents, multiplication, division, addition, and subtraction.
Take for example this expression:

$$
2*\frac{(3+5)^2}{x - y} +1
$$
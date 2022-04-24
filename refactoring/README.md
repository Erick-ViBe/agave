# Naming Refactor
Classes - PascalCase \
Methods - snake_case

# Code Refactor
  - A constructor was added in ParentClass, to have access to fullname, therefore it was possible to remove the parameter(fullname) from the methods that used it.
  - In the hey method of ChildClass, the 2 "elif" were replaced by "else", because the two decisions did the same thing.

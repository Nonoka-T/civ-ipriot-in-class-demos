# Readme

This is an example project, which you will recreate.

The aim here is to write nice unit tests.

# Here are some common pitfalls while running your unittests:
- [ ] Are modules importing correctly? If not:
	- [ ] Did you set your PYTHONPATH?
	- [ ] Are you running your project from the correct directory?
	- [ ] Does each subdirectory contain a `__init__.py` file? (This only affects some people)
- [ ] Are you running your tests using the unittest module correctly?
	- [ ] There are 2 ways -- letting the unittest module 'discover' tests (my preference), or running each test file as a script:
```python
if __name__ == "__main__":
    unittest.main()
```
		or

```bash
python -m unittest discover
```
- [ ] Did you name each test method starting with the word `test`? (I know 🙄, it's a little ridiculous)
- [ ] Does your unittest class inherit from unittest.TestCase?
- [ ] Are your assertions being called from 'self'? (eg: self.assertEquals)
- [ ] Do your test class names match the name of their file? Ie, if you have `TestBlog`, your file should be called `test_blog.py`

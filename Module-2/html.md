# HTML

### How are HTML and CSS used in the real world?
- **HTML (Hypertext Markup Language)**: Fundamental language for creating webpages, originally designed to share information. Evolved to support multimedia and responsive design.
- **CSS (Cascading Style Sheets)**: Manages webpage appearance and layout (color, fonts, spacing). Allows for features like media queries, transformations, and multiple backgrounds.
- **Combination Benefits**: Enables webpages to adapt to various devices (computers, smartphones, tablets, game consoles, smart TVs) and enhances design flexibility.
- **Standards**: Managed by W3C, with continuous updates to improve capabilities and support new requirements.


### Semantic tags and why we need them
- **Purpose of Semantic HTML**: Helps describe the meaning of web page content, similar to how numbers on elevator buttons indicate their function. Enhances understanding for search engines and accessibility tools (e.g., screen readers).

- **Basic Structure**: 
  - **HTML Page Layout**: Includes `<head>` and `<body>` tags.
  - **Semantic Tags**:
    - **`<header>`**: Contains site logo and navigation links.
    - **`<nav>`**: Defines navigation links, often used inside `<header>`.
    - **`<main>`**: Contains the primary content of the page.
    - **`<footer>`**: Includes contact info and social media links.

- **Main Content Elements**:
  - **`<article>`**: Represents a self-contained piece of content (e.g., blog posts, news articles). Use inside `<main>`.
  - **`<section>`**: Defines sections within an article or the page. Should include headings to describe sections.

- **Example Structure**:
  - **Header**: Includes site logo and `<nav>` with links.
  - **Main**: Contains `<article>` elements for individual pieces of content, with potential nested `<header>`, `<h1>`, and `<p>` tags.
  - **Footer**: Additional navigation or information.

- **Nesting and Flexibility**: Semantic elements can be nested as needed to accurately describe the content. Sections don’t always need to be inside articles; use them as appropriate.

- **Benefits**: Improved accessibility and SEO as content is clearly described and structured.


### Semantic HTML cheat sheet
---

There are hundreds of semantic tags available to help describe the meaning of your HTML documents. Below is a cheat sheet with some of the most common ones you’ll use in this course and in your development career.

*Sectioning tags* :
Use the following tags to organize your HTML document into structured sections. 

`<header>` :
The header of a content section or the web page. The web page header often contains the website branding or logo.

`<nav> `:
The navigation links of a section or the web page.

`<footer>` :
The footer of a content section or the web page. On a web page, it often contains secondary links, the copyright notice, privacy policy and cookie policy links.

`<main>` : Specifies the main content of a section or the web page.

`<aside>` :
A secondary set of content that is not required to understand the main content.

`<article>` : 
An independent, self-contained block of content such as a blog post or product.

`<section>` :
A standalone section of the document that is often used within the body and article elements.

`<details>` :
A collapsed section of content that can be expanded if the user wishes to view it.

`<summary>` :
Specifies the summary or caption of a `<details>` element.

`<h1><h2><h3><h4><h5><h6>` : 
Headings on the web page. `<h1>` indicates the most important heading whereas `<h6>` indicates the least important. 

**Content tags**
--

`<blockquote>` :
Used to describe a quotation.

`<dd>` :
Used to define a description for the preceding `<dt>` element.

`<dl>` :
Used to define a description list.

`<dt>` : 
Used to describe terms inside `<dl>` elements.

`<figcaption>` :
Defines a caption for a photo image.

`<figure>` :
Applies markup to a photo image.

`<hr>` :
Adds a horizontal line to the parent element.

`<li>` :
Used to define an item within a list.

`<menu>` :
A semantic alternative to `<ul>` tag.

`<ol>` :
Defines an ordered list.

`<p>` :
Defines a paragraph.

`<pre>` :
Used to represent preformatted text. Typically rendered in the web browser using a monospace font.

`<ul>` :
Unordered list

**Inline tags**
--

`<a>` : 
An anchor link to another HTML document.

`<abbr>` :
Specifies that the containing text is an abbreviation or acronym.

`<b>` :
Bolds the containing text. When used to indicate importance use `<strong>` instead.

`<br>` :
A line break. Moves the subsequent text to a new line.

`<cite>` :
Defines the title of creative work (for example a book, poem, song, movie, painting or sculpture). The text in the `<cite>` element is usually rendered in italics.

`<code>` :
Indicates that the containing text is a block of computer code.

`<data>` :
Indicates machine-readable data.

`<em>` :
Emphasizes the containing text.

`<i>` :
The containing text is displayed in italics. Used to indicate idiomatic text or technical terms.

`<mark>` :
The containing text should be marked or highlighted.

`<q>` :
The containing text is a short quotation.

`<s>` :
Displays the containing text with a strikethrough or line through it.

`<samp>` :
The containing text represents a sample.

`<small>` :
Used to represent small text, such as copyright and legal text.

`<span>` :
A generic element for grouping content for CSS styling.

`<strong>` :
Displays the containing text in bold. Used to indicate importance.

`<sub>` : 
The containing text is subscript text, displayed with a lowered baseline.

`<sup>` :
The containing text is superscript text, displayed with a raised baseline.

`<time>` :
A semantic tag used to display both dates and times.

`<u>` :
Displays the containing text with a solid underline.

`<var>` :
The containing text is a variable in a mathematical expression.

**Embedded content and media tags**
--

`<audio>` :
Used to embed audio in web pages.

`<canvas>` :
Used to render 2D and 3D graphics on web pages.

`<embed>` :
Used as a containing element for external content provided by an external application such as a media player or plug-in application. 

`<iframe>` :
Used to embed a nested web page. 

`<img>` :
Embeds an image on a web page.

`<object>` :
Similar to `<embed>` but the content is provided by a web browser plug-in.

`<picture>` :
An element that contains one `<img>` element and one or more `<source>` elements to offer alternative images for different displays/devices.

`<video>` :
Embeds a video on a web page.

`<source>` :
Specifies media resources for `<picture>`, `<audio>` and `<video>` elements.

`<svg>` :
Used to define Scalable Vector Graphics within a web page.

**Table tags**
--
`<table>` :
Defines a table element to display table data within a web page.

`<thead>` :
Represents the header content of a table. Typically contains one `<tr>` element.

`<tbody>` :
Represents the main content of a table. Contains one or more `<tr>` elements.

`<tfoot>` :
Represents the footer content of a table. Typically contains one `<tr>` element.

`<tr>` :
Represents a row in a table. Contains one or more `<td>` elements when used within `<tbody>` or `<tfoot>`. When used within `<thead>`, contains one or more `<th>` elements.

`<td>`
Represents a cell in a table. Contains the text content of the cell.

`<th>`
Defines a header cell of a table. Contains the text content of the header.

`<caption>`
Defines the caption of a table element.

`<colgroup>`
Defines a semantic group of one or more columns in a table for formatting.

`<col>`
Defines a semantic column in a table.

---
### What is Hyper Text Markup Language?
---
- **HTML Overview**: HTML (Hypertext Markup Language) is the fundamental structure of a web page, similar to a building frame guiding construction.

- **History**: Developed by Sir Tim Berners-Lee in 1991, with the first web page created in 1999 at CERN.

- **HTML Documents**: 
  - **File Type**: HTML files typically have a `.html` suffix (e.g., `index.html`).
  - **Structure**: Consists of elements and tags.

- **HTML Tags and Elements**:
  - **Tags**: Enclosed in angle brackets. Example: `<p>` for a paragraph.
  - **Elements**: Include opening and closing tags. Example: `<p>Content</p>`.
  - **Self-Closing Tags**: Do not have a closing tag. Example: `<br>` for a line break.

- **HTML Specification**: 
  - Maintained by the World Wide Web Consortium (W3C).
  - Current version: HTML5.

- **Function**: HTML elements and tags structure a web page and instruct the browser on how to display content. CSS is used for styling the page’s appearance.

---
### Semantic tags in action
---
**Adding a Blog Page with Semantic HTML**

1. **Basic Structure**: Created `blog.html` with semantic elements for accessibility and SEO.
   - **`<header>`**: Includes the Little Lemon logo using an `<img>` tag.
   - **`<nav>`**: Contains navigation links in an unordered list (`<ul>`), with list items (`<li>`) and anchor tags (`<a>`).
   - **`<main>`**: Hosts the primary content, including blog posts.
   - **`<footer>`**: Displays copyright information in a `<p>` tag.

2. **Content Details**:
   - **Header**: Added logo image.
   - **Navigation**: Links to `index.html`, `location.html`, and `blog.html`.
   - **Main**:
     - **`<h1>`**: Blog heading.
     - **`<article>`**: Two blog posts.
       - **First Article**: 
         - **`<h2>`**: Title "20% off this weekend".
         - **`<p>`**: Blog post text.
       - **Second Article**:
         - **`<h2>`**: Title "Our new menu".
         - **`<p>`**: Blog post text.
   - **Footer**: Added a paragraph for the copyright notice.

3. **Preview**: Saved the file and previewed it to ensure proper display and functionality.

**Outcome**: The blog page is now semantically structured, enhancing accessibility and SEO, and ensuring a positive experience for users and search engines.

---
### Forms And Validation
---
- **Purpose of Form Validation**: Ensures user input is accurate and meets predefined rules to prevent issues (e.g., incorrect delivery addresses).

- **Types of Validation**:
  - **Client-Side Validation**:
    - **When**: Checks errors as the user types or submits the form.
    - **Method**: Performed by the web browser or JavaScript.
    - **Feedback**: Immediate error messages guide users to correct mistakes.
    - **Examples**: Input type attributes such as `email` for validating email addresses, `tel` for telephone numbers, `url` for URLs, and `number` for numeric values.
    - **Attributes**: The `required` attribute ensures that a field must be filled out before submission.

  - **Server-Side Validation**:
    - **When**: Validates data after submission to the web server.
    - **Method**: Performed on the server, ensuring security and data integrity.
    - **Checks**: Can include database verification and complex business rules.
    - **Purpose**: Protects against tampering and ensures correct data processing.

- **Combining Methods**: Most websites use both client-side and server-side validation to provide user feedback and ensure data security and integrity.

**Key HTML Input Types for Validation**:
- **`email`**: Validates email addresses.
- **`tel`**: Validates telephone numbers.
- **`url`**: Validates URLs.
- **`date`**: Validates date values.
- **`time`**: Validates time values.
- **`number`**: Validates numeric values.
- **`range`**: Validates numeric values within a specified range.
- **`color`**: Validates color selection.

**Summary**: Form validation is crucial for accurate data entry and user experience. HTML provides basic client-side validation, while server-side validation ensures data integrity and security.


---
### Input types:
---

### 1. **Text**
Used for single-line text input.
```html
<input type="text" name="username" placeholder="Enter your username">
```

### 2. **Password**
Used for password input, obscures the text entered.
```html
<input type="password" name="password" placeholder="Enter your password">
```

### 3. **Email**
For entering email addresses, with validation.
```html
<input type="email" name="email" placeholder="Enter your email">
```

### 4. **Number**
For entering numeric values.
```html
<input type="number" name="age" placeholder="Enter your age" min="0" max="120">
```

### 5. **Date**
For selecting a date.
```html
<input type="date" name="birthdate">
```

### 6. **Checkbox**
Allows multiple options to be selected.
```html
<input type="checkbox" name="subscribe" value="newsletter"> Subscribe to newsletter
```

### 7. **Radio**
Allows only one option to be selected from a group.
```html
<input type="radio" name="gender" value="male"> Male
<input type="radio" name="gender" value="female"> Female
```

### 8. **Button**
For clickable buttons.
```html
<input type="button" value="Click Me">
```

### 9. **Submit**
Submits the form.
```html
<input type="submit" value="Submit">
```

### 10. **Reset**
Resets the form fields to their default values.
```html
<input type="reset" value="Reset">
```

### 11. **File**
For file uploads.
```html
<input type="file" name="fileupload">
```

### 12. **Range**
For selecting a value within a range.
```html
<input type="range" name="volume" min="0" max="100" step="1">
```

### 13. **Color**
For selecting a color.
```html
<input type="color" name="favcolor">
```

### 14. **Tel**
For entering telephone numbers.
```html
<input type="tel" name="phone" placeholder="Enter your phone number">
```

### 15. **Search**
For search queries, similar to text but with additional styling.
```html
<input type="search" name="search" placeholder="Search...">
```

### 16. **URL**
For entering URLs, with validation.
```html
<input type="url" name="website" placeholder="Enter your website URL">
```

### 17. **Datetime-local**
For entering date and time, including time zone.
```html
<input type="datetime-local" name="meeting">
```

### 18. **Month**
For selecting a month and year.
```html
<input type="month" name="birthday">
```

### 19. **Week**
For selecting a week and year.
```html
<input type="week" name="week">
```

Each input type is designed to handle specific kinds of user input and offer a range of functionality and validation based on the data being collected.

---
### Form Submission
---

**Form Submission Overview**: When you submit a form online, such as placing an order, the web browser sends the form data to the web server. This process involves an HTTP request and response cycle.

**HTTP Methods for Form Submission**:
  - **GET Method**:
    - **How It Works**: Form data is appended to the URL as query parameters.
    - **Example**: When clicking the submit button, data like username and password are included in the URL (e.g., `example.com/login?username=JohnDoe&password=1234`).
    - **Problems**:
      - **URL Length Limitation**: Limited to about 2,000 characters in most browsers, and 4,096 characters in some web servers. Large forms may result in truncated data.
      - **Security Risk**: Data is visible in the browser's URL history and server logs, posing privacy risks for sensitive information.

  - **POST Method**:
    - **How It Works**: Form data is sent in the body of the HTTP request.
    - **Example**: When the submit button is clicked, the data is included in the request body, not in the URL.
    - **Advantages**:
      - **Larger Data Capacity**: No practical limit on data size compared to GET.
      - **Enhanced Security**: Data is not visible in the URL, reducing exposure in browser history and server logs.
      - **Encryption**: For complete security, HTTPS is used to encrypt the data during transmission.

- **Response Handling**: After data submission, the web server processes the request and sends an HTTP response. If successful, the browser is directed to a new page. Errors can be handled in various ways on the webpage.

**Summary**: 
- **GET Method**: Data in URL, limited length, less secure.
- **POST Method**: Data in request body, larger capacity, more secure with HTTPS.

Understanding these methods helps in choosing the appropriate method for different types of data and ensuring secure and efficient data handling.

Certainly! Here’s a comprehensive overview of HTML forms, including details on submit types, HTTP methods, and alternative data submission methods:

---

## HTML Forms and Data Submission

### HTML Form Elements

1. **Submit Button**
   - **Purpose:** Submits the form data to the server.
   - **Example:**
     ```html
     <form action="/submit" method="post">
       <input type="submit" value="Submit">
     </form>
     ```

2. **Image Button**
   - **Purpose:** Uses an image as a submit button.
   - **Example:**
     ```html
     <form action="/submit" method="post">
       <input type="image" src="submit-button.png" alt="Submit">
     </form>
     ```

3. **Button with JavaScript**
   - **Purpose:** Uses a button element with JavaScript to submit the form programmatically.
   - **Example:**
     ```html
     <form id="myForm" action="/submit" method="post">
       <button type="button" onclick="document.getElementById('myForm').submit();">Submit</button>
     </form>
     ```

4. **Reset Button**
   - **Purpose:** Resets all form fields to their default values. (Not a submit button but often included in forms.)
   - **Example:**
     ```html
     <form action="/submit" method="post">
       <input type="reset" value="Reset">
     </form>
     ```

5. **Submit Button with Form Attributes**
   - **Purpose:** Allows overriding of the form’s action, method, or target directly on a `<button>` element.
   - **Example:**
     ```html
     <form action="/submit" method="post">
       <button type="submit" formaction="/another-endpoint" formmethod="get">Submit with GET</button>
     </form>
     ```

### HTTP Methods for Form Submission

**GET Method:**
- **Behavior:** The data from the form is encoded in the URL query string.
- **Use Case:** Suitable for requesting data from the server without changing server state, such as search forms.
- **Example:**
  ```html
  <form action="/search" method="get">
    <input type="text" name="query" placeholder="Search...">
    <input type="submit" value="Search">
  </form>
  ```

**POST Method:**
- **Behavior:** The data is sent in the body of the HTTP request.
- **Use Case:** Used for submitting data that modifies server state, such as registration or login forms.
- **Example:**
  ```html
  <form action="/submit" method="post">
    <input type="text" name="username" placeholder="Enter username">
    <input type="password" name="password" placeholder="Enter password">
    <input type="submit" value="Submit">
  </form>
  ```

### Processing Form Submissions

When a server receives a form submission, it processes the data based on the HTTP method (GET or POST). The server then returns a response indicating whether the submission was successful or if there were issues with the provided data.

### Alternative Data Submission Methods

HTML forms are not the only way to submit data to a server. JavaScript and front-end libraries offer more dynamic methods for handling data submission.

- **JavaScript for HTTP Requests:** Allows direct submission of HTTP requests, often using JSON for data exchange.
- **Example with Fetch API:**
  ```javascript
  fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'exampleUser',
      password: 'examplePass'
    }),
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
  ```

### Practice

Experiment with building various HTML forms and submitting data using different attributes and methods. Understand the use cases for GET and POST methods and explore JavaScript and libraries for advanced data submission techniques. This will help you develop robust and user-friendly web applications.

**Additional resources**

The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this section. 

 - [HTML meta tags](https://www.dofactory.com/html/metatags)
- [Semantic elements](https://www.freecodecamp.org/news/semantic-html5-elements/)
- [Client-side validation of forms with HTML5](https://www.sitepoint.com/client-side-form-validation-html5/)
- [`<input>` tag in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
- [Form validation examples](https://www.the-art-of-web.com/html/html5-form-validation/)
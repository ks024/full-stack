# Front-End Technologies

**Learning Objectives:**
* Recognize semantic HTML and basic forms
* Describe CSS and responsive layouts
* Update an HTML document using JavaScript

### Table of Contents
  - [HTML Summary](#HTML-Summary)
  - [Summary on CSS Layouts and Styling](#Summary-on-CSS-Layouts-and-Styling)


## HTML Summary

- **HTML and CSS Usage**: HTML structures webpages, evolving from simple text to supporting multimedia and responsive design. CSS styles these pages, managing layout and appearance across various devices, and is governed by W3C standards.

- **Semantic HTML**: Uses meaningful tags to improve content structure, accessibility, and SEO. Key semantic tags include `<header>`, `<nav>`, `<main>`, `<footer>`, `<article>`, and `<section>`. They help describe the content's meaning and enhance understanding for both users and search engines.

- **HTML Tags Cheat Sheet**:
  - **Sectioning Tags**: `<header>`, `<nav>`, `<footer>`, `<main>`, `<aside>`, `<article>`, `<section>`, `<details>`, `<summary>`.
  - **Content Tags**: `<blockquote>`, `<dd>`, `<dl>`, `<dt>`, `<figcaption>`, `<figure>`, `<hr>`, `<li>`, `<menu>`, `<ol>`, `<p>`, `<pre>`, `<ul>`.
  - **Inline Tags**: `<a>`, `<abbr>`, `<b>`, `<br>`, `<cite>`, `<code>`, `<data>`, `<em>`, `<i>`, `<mark>`, `<q>`, `<s>`, `<samp>`, `<small>`, `<span>`, `<strong>`, `<sub>`, `<sup>`, `<time>`, `<u>`, `<var>`.
  - **Embedded Media Tags**: `<audio>`, `<canvas>`, `<embed>`, `<iframe>`, `<img>`, `<object>`, `<picture>`, `<video>`, `<source>`, `<svg>`.
  - **Table Tags**: `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<td>`, `<th>`, `<caption>`, `<colgroup>`, `<col>`.

- **Form and Validation**:
  - **Validation**: Ensures accurate user input with client-side (immediate feedback using HTML attributes) and server-side (post-submission checks) validation. Key input types include `email`, `tel`, `url`, `number`, `date`, `checkbox`, `radio`, `submit`, and `file`.
  - **Submission Methods**: `GET` (data in URL, less secure) vs. `POST` (data in request body, more secure). Choose based on data type and security needs.

- **Form Submission**: Forms send data to servers using HTTP methods. `GET` appends data to the URL, while `POST` includes it in the request body. JavaScript can also handle submissions dynamically.

**For further reading:**
- [HTML meta tags](https://www.dofactory.com/html/metatags)
- [Semantic elements](https://www.freecodecamp.org/news/semantic-html5-elements/)
- [Client-side validation of forms with HTML5](https://www.sitepoint.com/client-side-form-validation-html5/)
- [`<input>` tag in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
- [Form validation examples](https://www.the-art-of-web.com/html/html5-form-validation/)

---
## Summary on CSS Layouts and Styling

**CSS Web Layouts**
- **Display Property**: 
  - **Block**: Elements stack vertically.
  - **Inline**: Elements stack horizontally.
- **Flexbox**: 
  - Manages one-dimensional layouts (rows or columns).
  - Allows items to grow or shrink, creating flexible designs.
- **Grid Layout**: 
  - Manages two-dimensional layouts (rows and columns).
  - Ideal for complex layouts with precise control.
- **Choosing Layouts**:
  - **Flexbox**: Suitable for small, flexible designs.
  - **Grid**: Suitable for large, complex layouts.
  - Can be used together on a page for optimal results.

**Widely Used Selectors**
- **Element Selectors**: Target elements by type (e.g., `p`, `h1`).
- **ID Selectors**: Target elements with a unique ID (e.g., `#header`).
- **Class Selectors**: Target elements with a specific class (e.g., `.button`).
- **Attribute Selectors**: Style elements based on attributes (e.g., `[href*="meta"]`).
- **Nth-of-Type and Nth-Child Selectors**: Target specific children within a parent (e.g., `:nth-of-type(2)`).

**CSS Units of Measurement**
- **Absolute Units**: Fixed size, useful for print (e.g., `px`, `cm`).
- **Relative Units**: Relative to other elements or viewport (e.g., `em`, `vw`, `vh`).
- **Practice**: Helps choose the best units for various properties.

**Document Flow: Block vs. Inline**
- **Block-Level Elements**: Full width, start on a new line (e.g., `<div>`).
- **Inline Elements**: Width depends on content, do not start on a new line (e.g., `<span>`).
- **CSS `display` Property**: Switches between block and inline behavior.

**Basic Flexbox**
- **Search Bar**: Use `display: inline-flex;` for container, align items with Flexbox properties.
- **Navigation Menu**: Apply `flex-flow` for direction and wrapping, ensure responsiveness.
- **Image Gallery**: Use `display: flex;`, `flex-wrap` for wrapping, and `justify-content` for spacing.

**CSS Grids**
- **Two-Dimensional Layout**: Uses rows and columns.
- **Grid Container Properties**: Define columns, rows, and gaps with properties like `grid-template-columns`, `grid-gap`.
- **Advanced Functions**: `repeat` and `minmax` functions for efficient layout definition.
- **Grid Frameworks**: Common 12-column and 16-column grids for structured layouts.

**CSS Grid and Flexbox Cheat Sheet**
- **Grid**: 
  - `display: grid;`, `grid-template-columns`, `grid-template-rows`.
  - Alignment with `justify-items`, `align-items`, and spacing with `grid-gap`.
- **Flexbox**:
  - `display: flex;`, `flex-direction`, `justify-content`, and `align-items`.
  - Control item sizing with `flex-grow`, `flex-shrink`, and `flex-basis`.

**CSS Specificity Overview**
- **Specificity Hierarchy**: Inline styles > IDs > Classes/Attributes/Pseudo-classes > Elements/Pseudo-elements.
- **Calculating Specificity**: Use values for each selector type to determine which styles apply.
- **CSS Specificity Calculators**: Tools to help manage specificity conflicts.

**Pseudo-Class Selectors**
- **User Action States**: `:hover`, `:active`, `:focus`.
- **Form States**: `:disabled`, `:enabled`, `:checked`, `:valid`, `:invalid`.
- **Position-Based States**: `:first-of-type`, `:last-of-type`, `:nth-of-type(n)`.

**Pseudo-Elements in CSS**
- **`::first-letter`**: Styles the first letter of an element.
- **`::first-line`**: Styles the first line of an element.
- **`::selection`**: Styles selected text.
- **`::marker`**: Styles list item markers.
- **`::before` and `::after`**: Add content before or after an element’s content.

**Additional Resources**
- CSS layouts overview, Flexbox and Grid guides, selectors and pseudo-classes references, and more detailed explanations on specific CSS features.

### Here are some valuable resources to further explore CSS concepts:

- **Broad Overview of Layouts in CSS**: [MDN Web Docs on CSS Layout](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout) provides a general introduction to CSS layout techniques, including flexbox and grid.
  
- **Detailed Overview of Flexboxes**: [CSS-Tricks Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) offers an in-depth look at flexbox, including its properties and practical applications.

- **Detailed Overview of CSS Grids (1)**: [Learn CSS Grid](https://learncssgrid.com/) covers the basics and advanced features of CSS Grid Layout, with interactive examples.

- **Detailed Overview of CSS Grids (2)**: [Web.dev Guide to CSS Grid](https://web.dev/learn/css/grid/) provides a comprehensive tutorial on CSS Grid Layout with modern practices.

- **Commonly Used Selectors**: [GeeksforGeeks on CSS Selectors](https://www.geeksforgeeks.org/10-css-selectors-every-developer-should-know/) highlights essential CSS selectors and their uses.

- **Combinator Selectors**: [MDN Web Docs on Combinators](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators) explains combinator selectors that define relationships between elements.

- **Comprehensive List of Selectors**: [W3Schools CSS Selectors](https://www.w3schools.com/cssref/css_selectors.asp) provides a thorough list of CSS selectors and their functionalities.

- **Comprehensive List of Pseudo-Classes**: [MDN Web Docs on Pseudo-Classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) details pseudo-classes that style elements based on their state.

- **Comprehensive List of Pseudo-Elements**: [MDN Web Docs on Pseudo-Elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements) explains pseudo-elements for targeting specific parts of elements or adding content.
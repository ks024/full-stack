# CSS

### CSS Web Layouts

CSS (Cascading Style Sheets) enhances web design by controlling the visual presentation of web pages, including layout, fonts, and colors. Understanding CSS layout techniques is crucial for creating well-organized and responsive web pages.

- **Display Property**: Determines how elements are rendered:
  - **Block**: Elements stack vertically.
  - **Inline**: Elements stack horizontally.

- **Flexbox**: 
  - Manages one-dimensional layouts (rows or columns).
  - Creates flexible, responsive designs where items can grow or shrink.

- **Grid Layout**: 
  - Manages two-dimensional layouts (rows and columns).
  - Useful for complex layouts but requires careful structuring.

- **Choosing Layouts**:
  - **Flexbox**: Best for small, flexible designs.
  - **Grid**: Best for large, complex layouts.
  - Both can be used together on a single page.

CSS layout rules are standardized but offer flexibility for creative and optimized web design, enabling developers to craft visually appealing and functional websites.

---
### Widely Used Selectors

**CSS Selectors Overview**

In this video, you revisited commonly used CSS selectors and explored some new ones to enhance your web styling capabilities.

- **Previously Covered Selectors:**
  - **Element (Type) Selectors**: Target elements based on their type (e.g., `p`, `h1`).
  - **ID Selectors**: Target elements with a unique ID (e.g., `#header`).
  - **Class Selectors**: Target elements with a specific class (e.g., `.button`).

- **Newly Covered Selectors:**
  - **Attribute Selectors**: Style elements based on their attributes and values. For example:
    - `[class]` targets elements with a class attribute.
    - `[href*="meta"]` targets elements where the `href` attribute contains the word "meta."
    - `[href="specific-link"]` targets elements with a specific `href` value.

  - **Nth-of-Type and Nth-Child Selectors**: Target specific children of a parent element.
    - `:nth-of-type(n)` targets the nth element of a specific type.
    - `:nth-child(n)` targets the nth child element, regardless of type.

  - **Star Selector (`*`)**: Selects all elements on the page. Useful for resetting default styles.

  - **Group Selectors**: Apply the same styles to multiple elements. For example:
    - `h1, p { color: blue; }` applies the same style to both `<h1>` and `<p>` elements.

Understanding these selectors improves your ability to precisely target and style elements, enhancing your web design process. In the next lesson, you'll delve into more advanced selectors to further expand your styling toolkit.

---
### CSS Units of Measurement

**1. Absolute Units**  
- **Constant across devices; fixed size.**  
- **Commonly used for print or when size remains constant.**  
  - **Q**: Quarter-millimeters (1Q = 1/40 cm)  
  - **mm**: Millimeters (1mm = 1/10 cm)  
  - **cm**: Centimeters (1cm = 37.8px)  
  - **in**: Inches (1in = 2.54cm = 96px)  
  - **pc**: Picas (1pc = 1/6 in)  
  - **pt**: Points (1pt = 1/72 in)  
  - **px**: Pixels (1px = 1/96 in)  

**2. Relative Units**  
- **Defined relative to other elements or viewport size.**  
- **Preferred for dynamic web pages and responsive designs.**  
  - **em**: Font size of the parent element.  
  - **ex**: Height of the 'x' character of the font.  
  - **ch**: Width of the font character.  
  - **rem**: Font size of the root element.  
  - **lh**: Line height of the parent element.  
  - **rlh**: Line height of the root element.  
  - **vw**: 1% of viewport width.  
  - **vh**: 1% of viewport height.  
  - **vmin**: 1% of the smaller viewport dimension.  
  - **vmax**: 1% of the larger viewport dimension.  
  - **%**: Percentage relative to the parent element.  

**Note:**  
- **Absolute units are useful for print and fixed-size scenarios.**  
- **Relative units are ideal for responsive and flexible designs.**  
- **Certain CSS properties have specific acceptable values (e.g., color values).**  
- **Practice with different units will help determine the best choice for various properties.**

---
### Document flow - block vs. inline
**CSS Layout and Document Flow Summary**

In this video, you explored how CSS styles HTML elements and how browsers determine element placement on the screen through document flow. 

- **Document Flow**: The default method browsers use to arrange HTML elements on the page. Elements are categorized into two types:

  - **Block-Level Elements**: 
    - Occupy the full width of their parent container and the height of their content.
    - Start on a new line and stack vertically.
    - Examples: `<div>`, `<form>`, `<h1>`, etc.

  - **Inline Elements**: 
    - Only take up as much width as their content requires.
    - Do not start on a new line and can be placed next to each other.
    - Examples: `<a>`, `<img>`, `<span>`, etc.

- **Example Demonstration**:
  - **HTML Structure**: Using `<div>` and `<span>` elements to illustrate document flow.
  - **Effect of Block vs. Inline**: Changing a `<span>` to a `<div>` moves the text to a new line due to block behavior. Conversely, converting a `<div>` to inline using CSS places it in the same line as surrounding content.

- **CSS `display` Property**:
  - Allows switching between block and inline behavior.
  - Example: Setting `display: inline;` on a `<div>` changes its behavior to inline, and removing or setting `display: block;` reverts it to block behavior.

Understanding these concepts is crucial for effective web design, as block elements manage vertical spacing, while inline elements manage horizontal alignment within text flow.

---
### Basic Flexbox
**Flexbox Practical Applications Summary**

In this video, you learned about common uses of Flexbox for creating responsive and flexible web layouts. Here are the three primary examples of Flexbox applications discussed:

1. **Search Bar**:
   - **Structure**: Consists of a search icon, search input area, and a submit button.
   - **CSS Implementation**: 
     - Use `display: inline-flex;` for the container to make it behave like an inline element.
     - Apply `overflow` to handle text input clipping.
     - Align items using Flexbox properties to ensure the search bar looks cohesive and responsive.

2. **Navigation Menu**:
   - **Structure**: An unordered list with multiple items.
   - **CSS Implementation**: 
     - Use the universal selector `*` to reset browser-specific formatting.
     - Apply `flex-flow` to control the direction and wrapping of flex items.
     - Use `justify-content: stretch;` to align items along the main axis.
     - Ensure responsiveness so that items stack vertically on smaller screens and align horizontally on larger screens.

3. **Image Gallery**:
   - **Structure**: A container with multiple images.
   - **CSS Implementation**:
     - Set `display: flex;` on the container.
     - Use `flex-wrap` to allow items to wrap onto new lines.
     - Apply `justify-content: space-between;` to distribute images evenly.
     - Reset browser-specific styles for margins, padding, and borders.

These examples demonstrate how Flexbox can efficiently handle layout challenges by aligning and distributing elements responsively. Flexbox is especially useful for creating adaptable and organized web designs.

---
### CSS Grids

**CSS Grid Layouts Summary**

In this video, you explored the CSS Grid layout system, a powerful tool for designing responsive and organized web pages. Here's a summary of the key concepts and steps covered:

- **CSS Grid Basics**:
  - **Two-Dimensional Layout**: CSS Grid enables the design of layouts using both rows and columns, offering more control than Flexbox.
  - **Columns and Rows**: Grids divide the viewport into vertical columns and horizontal rows. The intersections create cells where content is placed.
  - **Gutters**: The space between columns and rows is called gutters or gaps.

- **Example Demonstration**:
  - **Initial HTML**: A basic HTML document displaying letters without any styling.
  - **CSS Grid Setup**:
    - **Display Property**: Set `display: grid;` on the container to enable grid layout.
    - **Grid Template Columns/Rows**: Define columns and rows using pixel values or the `fr` (fraction) unit for flexible sizing.
    - **Grid Gap**: Add `grid-gap` or `gap` to set the space between grid cells.
    - **Auto Rows/Columns**: Use `grid-auto-rows` and `grid-auto-columns` to automatically size rows and columns.

- **Advanced Grid Functions**:
  - **Repeat Function**: Simplifies code by specifying how many times to repeat grid columns or rows.
    - Example: `grid-template-columns: repeat(3, 1fr);` creates three equal columns.
  - **Min-Max Function**: Sets minimum and maximum sizes for rows and columns.
    - Example: `grid-template-rows: minmax(150px, auto);` ensures rows are at least 150px tall but can grow.

- **Grid Frameworks**:
  - **12-Column and 16-Column Grids**: Common frameworks that divide the page into 12 or 16 columns, respectively, allowing for flexible and structured layouts.

CSS Grid provides a robust framework for designing complex and adaptable layouts, making it easier to present content in a visually appealing manner. By using properties like `repeat`, `minmax`, and grid frameworks, you can streamline your coding process and enhance the responsiveness of your web pages.

---

### CSS Grid and Flexbox Cheat Sheet

#### **CSS Grid**

**Syntax for Creating a Grid:**
```css
selector {
    display: grid; /* or inline-grid */
}
```

**Grid Container Properties:**
- `grid-template-columns`: Defines column sizes (e.g., `100px`, `25%`, `repeat(3, 1fr)`).
- `grid-template-rows`: Defines row sizes (e.g., `100px`, `25%`, `repeat(3, 1fr)`).
- `grid-template-areas`: Names and positions grid areas.
- `grid-auto-rows`: Default size for rows not explicitly defined.
- `grid-auto-columns`: Default size for columns not explicitly defined.
- `grid-auto-flow`: Determines item placement (e.g., `row`, `column`, `dense`).
- `grid-gap` / `grid-column-gap` / `grid-row-gap`: Sets gaps between rows and columns.

**Alignment:**
- `justify-items`: Aligns items in their grid areas (e.g., `start`, `center`, `end`, `stretch`).
- `align-items`: Aligns items along the grid’s block axis (e.g., `start`, `center`, `end`, `stretch`).
- `place-items`: Shorthand for `justify-items` and `align-items`.

**Justification:**
- `justify-content`: Aligns the entire grid in the container (e.g., `start`, `center`, `end`, `space-between`, `space-evenly`, `space-around`).
- `align-content`: Aligns content along the cross axis (e.g., `start`, `center`, `end`, `space-between`, `space-evenly`, `space-around`).
- `place-content`: Shorthand for `justify-content` and `align-content`.

**Item Positioning:**
- `grid-column`: Defines column span (e.g., `1 / 3`).
- `grid-row`: Defines row span (e.g., `1 / 3`).
- `grid-column-start`, `grid-column-end`, `grid-row-start`, `grid-row-end`: Specific positions for grid items.

**Gap:**
- `grid-gap`: Sets the gap between rows and columns.

**Example:**
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr;
    grid-template-rows: auto 1fr;
    grid-template-areas: "header header" "main aside" "footer footer";
    gap: 10px;
}
```

#### **CSS Flexbox**

**Syntax for Creating a Flexbox:**
```css
selector {
    display: flex; /* or inline-flex */
}
```

**Flex Container Properties:**
- `flex-direction`: Direction of items (e.g., `row`, `row-reverse`, `column`, `column-reverse`).
- `flex-wrap`: Determines item wrapping (e.g., `wrap`, `nowrap`).
- `align-items`: Aligns items on the cross axis (e.g., `flex-start`, `flex-end`, `center`, `stretch`).
- `justify-content`: Aligns items on the main axis (e.g., `flex-start`, `flex-end`, `center`, `space-between`, `space-evenly`).

**Flex Item Properties:**
- `flex-grow`: Defines how much a flex item should grow relative to other items.
- `flex-shrink`: Defines how much a flex item should shrink relative to other items.
- `flex-basis`: Initial size of a flex item (e.g., `auto`, `100px`).
- `order`: Specifies the order of the flex items.
- `align-self`: Aligns an item within its flex container (e.g., `start`, `center`, `end`, `stretch`).

**Example:**
```css
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.item {
    flex: 1;
}
```

This cheat sheet covers the basics of CSS Grid and Flexbox properties to help with layout design.

---

### CSS Specificity Overview

**CSS Specificity** helps determine which CSS rules are applied when multiple rules conflict. It is a hierarchical system that ranks selectors based on their specificity. Higher specificity values override lower ones.

#### Specificity Hierarchy

1. **Inline Styles**: 
   - Highest specificity.
   - Example: `<p style="color: white;">`
   - Specificity Score: 1000 (or `1 0 0 0`).

2. **IDs**:
   - Represented by `#`.
   - Example: `#header`
   - Specificity Score: 0100 (or `0 1 0 0`).

3. **Classes, Attributes, and Pseudo-classes**:
   - Classes: `.class-name`
   - Attributes: `p[attribute]`
   - Pseudo-classes: `:hover`
   - Specificity Score: 0010 (or `0 0 1 0`).

4. **Elements and Pseudo-elements**:
   - Elements: `div`, `p`
   - Pseudo-elements: `::before`, `::after`
   - Specificity Score: 0001 (or `0 0 0 1`).

#### Calculating Specificity

Specificity is calculated by adding values for each category of selector types:

1. **Inline styles:** Highest value, `1000`
2. **IDs:** Next highest, `100`
3. **Classes, attributes, pseudo-classes:** Intermediate value, `10`
4. **Elements, pseudo-elements:** Lowest value, `1`

**Example Calculation:**

- `#hello {}`  
  Specificity: `0100`

- `div {}`  
  Specificity: `0001`

- `div p.foo {}`  
  Specificity: `0012`  
  (2 elements + 1 class)

**Examples:**

1. **Example 1**:
   - `p {}`  
     Specificity: `0001`
   - `div p {}`  
     Specificity: `0002`
   - `div p.foo {}`  
     Specificity: `0012`  
   The rule with the highest specificity, `div p.foo`, will be applied.

2. **Example 2**:
   - `p#bar`  
     Specificity: `0101`  
     (1 element + 1 ID)
   - `p.foo`  
     Specificity: `0011`  
     (1 element + 1 class)
   - `p.p.foo`  
     Specificity: `0021`  
     (1 element + 2 classes)  
   The rule with the highest specificity, `p.p.foo`, will be applied.

#### Additional Guidelines

- **Selectors with Equal Specificity:** The last written rule is applied.
- **ID Selectors:** Should be used sparingly to ensure high specificity where needed.
- **Universal Selector (`*`):** Zero specificity.
- **CSS Specificity Calculators:** Useful tools for determining rule precedence.

Understanding specificity helps manage conflicts and ensures the intended styles are applied correctly.

---
### Pseudo-Class Selectors Overview

**Pseudo-class selectors** enhance CSS by allowing developers to style elements based on their state or position. These selectors provide advanced styling and interactivity without extra effort, improving user experience on web pages.

#### General Syntax

```css
selector:pseudo-class {
    property: value;
}
```

#### General Classifications

1. **User Action States**:
   - **`:hover`**: Styles an element when the cursor hovers over it.
     - *Example*: `a:hover { color: red; }`
   - **`:active`**: Styles an element while it is being pressed.
     - *Example*: `button:active { background-color: blue; }`
   - **`:focus`**: Styles an element when it receives focus.
     - *Example*: `input:focus { border: 2px solid green; }`

   **Example Usage**:
   ```html
   <a href="#" class="mypage">My Page</a>
   <button class="mybutton">Click Me</button>
   ```

   ```css
   .mypage:hover { color: red; }
   .mybutton:active { background-color: blue; }
   ```

2. **Form States**:
   - **`:disabled`**: Targets disabled form elements.
     - *Example*: `input:disabled { background-color: grey; }`
   - **`:enabled`**: Targets enabled form elements.
     - *Example*: `input:enabled { background-color: white; }`
   - **`:checked`**: Targets checked checkboxes or radio buttons.
     - *Example*: `input:checked { background-color: yellow; }`
   - **`:indeterminate`**: Targets checkboxes in an indeterminate state.
     - *Example*: `input:indeterminate { background-color: orange; }`
   - **`:valid`**: Targets valid form fields.
     - *Example*: `input:valid { border: 2px solid green; }`
   - **`:invalid`**: Targets invalid form fields.
     - *Example*: `input:invalid { border: 2px solid red; }`

3. **Position-Based States**:
   - **`:first-of-type`**: Targets the first element of its type within its parent.
     - *Example*: `li:first-of-type { font-weight: bold; }`
   - **`:last-of-type`**: Targets the last element of its type within its parent.
     - *Example*: `li:last-of-type { font-style: italic; }`
   - **`:nth-of-type(n)`**: Targets the nth element of its type within its parent.
     - *Example*: `li:nth-of-type(2) { color: green; }`
   - **`:nth-last-of-type(n)`**: Targets the nth element from the end of its type within its parent.
     - *Example*: `li:nth-last-of-type(1) { color: blue; }`

   **Example Usage**:
   ```html
   <ul>
       <li>Adrian</li>
       <li>Mario</li>
   </ul>
   ```

   ```css
   li:first-of-type { color: red; }
   ```

#### Practical Example

```html
<p>This is a paragraph.</p>
<input type="text" placeholder="Type something...">
<input type="checkbox" id="check1">
<input type="checkbox" id="check2" checked>
```

```css
input:focus { border: 2px solid blue; }
input:checked { background-color: yellow; }
p:first-of-type { color: green; }
```

### Summary

Pseudo-classes provide powerful tools for styling elements based on user interactions, form states, and positional context. By leveraging pseudo-classes like `:hover`, `:focus`, `:checked`, and `:nth-of-type`, you can create more dynamic and interactive web pages.

---
### Pseudo-Elements in CSS

Pseudo-elements are powerful tools in CSS that allow you to style specific parts of an element or add additional content without modifying the HTML. They help enhance the design and presentation of your web pages.

#### Syntax

The syntax for pseudo-elements involves using two colons (`::`) followed by the pseudo-element name:

```css
selector::pseudo-element {
    property: value;
}
```

### Common Pseudo-Elements

#### 1. `::first-letter`

Styles the first letter of an element. Useful for adding emphasis to the beginning of paragraphs or list items.

**Example:**

**HTML:**
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <ul>
        <li>Item one</li>
        <li>Item two</li>
        <li>Item three</li>
    </ul>
</body>
</html>
```

**CSS:**
```css
li::first-letter {
    color: coral;
    font-size: 1.3em;
    font-weight: bold;
    line-height: 1;
}
```

**Output:**

The first letter of each list item will be coral, larger, bold, and visually distinct.

#### 2. `::first-line`

Styles the first line of an element. This can be used to apply unique styles to the first line of a paragraph or list item.

**Example:**

**CSS:**
```css
ul {
    list-style-type: none;
}

li::first-line {
    color: lightseagreen;
    text-decoration: underline;
    line-height: 1;
}
```

**Output:**

The first line of each list item will be light sea green, underlined, and distinct from the rest of the text.

#### 3. `::selection`

Styles the portion of the element that the user has selected. Useful for improving the user experience by changing the appearance of selected text.

**Example:**

**CSS:**
```css
li::selection {
    color: brown;
    background-color: antiquewhite;
}
```

**Output:**

The selected text within list items will have a brown color with an antiquewhite background.

#### 4. `::marker`

Styles the marker of a list item (e.g., bullet points or numbers). This pseudo-element is helpful for customizing the appearance of list markers.

**Example:**

**CSS:**
```css
li::marker {
    color: cornflowerblue;
    content: '<> ';
    font-size: 1.1em;
}
```

**Output:**

The bullet points in the list will be cornflower blue with a custom symbol and slightly larger size.

#### 5. `::before` and `::after`

These pseudo-elements add content before or after an element’s content. They are often used to add decorative elements or additional information.

**Example:**

**HTML:**
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <p id="tips">Don't rinse your pasta after it is drained.</p>
    <p>Slice the tomatoes. Take the extra efforts to seed them.</p>
    <p id="tips">Peel and seed large tomatoes.</p>
</body>
</html>
```

**CSS:**
```css
#tips::before {
    content: "Tip:";
    background: darkkhaki;
    color: darkslategray;
    padding: 3px 5px;
    border-radius: 10%;
}

#tips::after {
    content: "!!";
    color: darkslategray;
    padding-left: 5px;
}
```

**Output:**

Each paragraph with the ID `tips` will have the word "Tip:" before it and "!!" after it, styled with specific colors and padding.

### Conclusion

Pseudo-elements are a versatile and powerful feature in CSS, allowing you to style specific parts of elements or add content dynamically. By using pseudo-elements like `::first-letter`, `::first-line`, `::selection`, `::marker`, and `::before`/`::after`, you can significantly enhance the visual appeal and user experience of your web pages.

Feel free to experiment with these pseudo-elements and explore their creative applications to suit your design needs.

---
## Additional resources
The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this section.

- [Broad overview of layouts in CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout)
- [Detailed overview of flexboxes](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Detailed overview of grids (1)](https://learncssgrid.com/)
- [Detailed overview of grids (2)](https://web.dev/learn/css/grid/)
- [Commonly used selectors](https://www.geeksforgeeks.org/10-css-selectors-every-developer-should-know/)
- [Combinator selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators)
- [Comprehensive list of selectors](https://www.w3schools.com/cssref/css_selectors.asp)
- [Comprehensive list of pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
- [Comprehensive list of pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)
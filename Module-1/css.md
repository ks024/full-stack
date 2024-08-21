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

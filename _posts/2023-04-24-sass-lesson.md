---
keywords: fastai
title: SASS
nb_path: _notebooks/2023-04-24-sass-lesson.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2023-04-24-sass-lesson.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Why-SASS?">Why SASS?<a class="anchor-link" href="#Why-SASS?"> </a></h1><p>SASS is an improvement on CSS in that there are methods of abstraction. It is a stylesheet language that is compiled into CSS, which means that Sass will translate the Sass code you wrote into CSS, which is what your web browser can read.</p>
<h1 id="SASS-vs-SCSS">SASS vs SCSS<a class="anchor-link" href="#SASS-vs-SCSS"> </a></h1><p>As you learn about Sass, you might notice something called Scss. They are basically the same thing except that Scss uses curly braces and semicolons to distinguish between lines. Sass uses indentation and newlines instead.</p>
<p>We will be teaching the Scss syntax because it is more commonly used.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Getting-started">Getting started<a class="anchor-link" href="#Getting-started"> </a></h1><p>A easy way to write SASS and have it preprocessed into CSS is by using a Jekyll powered website, such as GitHub pages or Fastpages.</p>
<p>The first step is to clone a GitHub pages repo, such as this <a href="https://github.com/lwu1822/sassy_squad">one</a>.</p>
<p>Within the repository, head over to <code>assets/css/</code>, and open <code>style.scss</code>.</p>
<p>This is where you can create your SASS code.</p>
<p>To see your CSS-translated SASS code, head over to <code>_site/assets/css/style.css</code></p>
<p>Note: You will need to run bundle exec jekyll serve before the _site directory appears.</p>
<p>The first few hundred lines are used to style Github's theme. Make sure to scroll to the very bottom to see the SASS code that you wrote, which is in the form of CSS.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Nesting">Nesting<a class="anchor-link" href="#Nesting"> </a></h1><ul>
<li>Many different selectors and objects may share the same element.</li>
<li>Through nesting, you can write the styling code in a heirarchy</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Mini-hack">Mini-hack<a class="anchor-link" href="#Mini-hack"> </a></h1><p>Write out the SASS equivalent for the following CSS code:</p>

<pre><code>.a .b {
    color: green;
}

.a .c {
    color: blue;
}</code></pre>
<p>SASS equivalent:</p>

<pre><code>.a {
    .b {
    color: green;

    .c {
    color: blue;
}}}</code></pre>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Extend/Inheritance">Extend/Inheritance<a class="anchor-link" href="#Extend/Inheritance"> </a></h1><p>What are some similarities that the buttons share? What are the differences?</p>
<p>Take notes here:</p>
<ul>
<li>The buttons have the same size - width, height</li>
<li>They also have the same font size and font color</li>
<li>The spacing of the buttons are also similar</li>
<li>The background colors of the buttons differ </li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Mixin">Mixin<a class="anchor-link" href="#Mixin"> </a></h1><ul>
<li>Creates a code template that can be reused</li>
<li>Can also accept parameters so that dynamic styling can be utilized</li>
<li>Create mixin through <code>@mixin</code> and call it through <code>@include</code></li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Mini-hack">Mini-hack<a class="anchor-link" href="#Mini-hack"> </a></h1><p>Write out a mixin in SASS that takes in a color and a font size as the parameter. Within the mixin, set the background color and font color to the color parameter, and set the font size to the font size parameter. Then create a selector that calls the mixin, and pass in a color and font size of your choice as the arguments.</p>
<p>SASS code:</p>

<pre><code>@mixin testCode($testColor, $fontSize) {
    background: $testColor;
    color: $testColor;
    font-size: $fontSize;
}
.testCodeSelector {
    @include testCode(#00ffc1, 10px);
}</code></pre>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Function">Function<a class="anchor-link" href="#Function"> </a></h1><p>Take notes here:</p>
<ul>
<li>Can be created in SASS using <code>@function</code></li>
<li>Like a function in a Python, it follows the format <code>functionName(Parameters)</code></li>
<li>There should also be brackets after, like a Javascript function</li>
<li>Are called by specifying the function name with parenthesis<ul>
<li>Inside the parenthesis, define the arguments that the function will take in as parameters</li>
</ul>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Import">Import<a class="anchor-link" href="#Import"> </a></h1><p>Take notes here:</p>
<ul>
<li>SASS code can be split into multiple files and imported into one file</li>
<li>For example, create a directory called <code>_sass</code><ul>
<li>You can create multiple files in here, such as <code>style.scss</code> and <code>color.scss</code></li>
<li>If you want the code from <code>style.scss</code> to be imported into <code>color.scss</code>, use the command <code>@import "style"</code></li>
<li>The <code>.scss</code> is not needed and there has to be quotation marks around the function name</li>
</ul>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="SASS-Hacks">SASS Hacks<a class="anchor-link" href="#SASS-Hacks"> </a></h1><ol>
<li><p>Take notes and complete the mini-hacks. (0.9)</p>
</li>
<li><p>Complete the <a href="https://lwu1822.github.io/sassy_squad/quizQuestions">quiz questions</a> and provide your answers in this notebook. (0.9)</p>
</li>
<li><p>Use SASS to create something that uses either extend or mixin. (0.9)</p>
</li>
<li><p>Extra credit: Research other SASS features and blog about what you learned or add to your SASS project with any extra features not covered in this lesson. More points will be given if both are done.</p>
</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Quiz-Answers">Quiz Answers<a class="anchor-link" href="#Quiz-Answers"> </a></h2><ol>
<li>B</li>
<li>A</li>
<li>C</li>
<li>B</li>
<li>D</li>
<li>B</li>
<li>B</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Researched-SASS-features">Researched SASS features<a class="anchor-link" href="#Researched-SASS-features"> </a></h2><p>Variables:</p>
<ul>
<li>Enables users to define values<ul>
<li>Can be used to define colors, font sizes, margins, padding values, and more.</li>
</ul>
</li>
</ul>
<p>Control Directives:</p>
<ul>
<li>Some examples are <code>@if</code>, <code>@for</code>, and <code>@each</code></li>
<li>These enable us to write conditional statements and loops, and also allow iteration</li>
</ul>
<p>Partials:</p>
<ul>
<li>Partial SASS files that contain small code segments</li>
<li>Can be included in other files</li>
<li>Is an easy way to organize code</li>
<li>Name with an underscore like <code>_partial.scss</code></li>
</ul>
<p>Modules:</p>
<ul>
<li>Can be used to split SASS code in a single file</li>
<li><code>@use</code></li>
<li>Loads another SASS file as a module<ul>
<li>Its variables, mixins, and functions can be accessed</li>
</ul>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><style>
    @mixin button {
    display: inline-block;
    padding: 10px 20px;
    border: 1px solid #f8057e;
    border-radius: 5px;
    background-color: #04f886;
    color: #1d1c1c;
    text-align: center;
    text-decoration: none;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;</p>

<pre><code>&amp;:hover {
  background-color: #ccc;
  color: #fff;
}
</code></pre>
<p>}
  .primary-btn {
    @include button;
    //background-color: #007bff;
    //color: #fff;
  }</p>
<p>.secondary-btn {
    @extend .primary-btn;
    //background-color: #6c757d;
  }</p>
<p>&lt;/style&gt;</p>
<html>
<head>
</head>
    <body>
        <div class="button">
            <button class="primary-btn">First Button</button>
            <button class="secondary-btn">Second Button</button>
        </div>
    </body>
</html>
</div>
</div>
</div>
</div>
 

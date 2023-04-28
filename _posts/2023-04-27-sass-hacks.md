---
toc: true
layout: post
title: SASS Hacks
categories: [markdown, Week 31]
---
<style>
@mixin button-styles {
  font-size: 1.2em;
  padding: 30px 50px;
  color: #fff;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.4);
  border: none;
  border-radius: 30px;
  cursor: pointer;
  background: linear-gradient(to right, #00c6ff, #0072ff);
  transition: all 0.2s ease-in-out;
}

.button {
  @include button-styles; 
  width: 25%;
  height: 150px;
  margin: auto;
  margin-bottom: 20px;
  border-radius: 30px;
  background-image: linear-gradient(to bottom left, #1EEACB, #0BE564);
  &:hover {
    transform: scale(1.2);
  }
}

.special-button {
  @include button-styles;
  width: 25%;
  height: 150px;
  margin: auto;
  border-radius: 30px;
  background: linear-gradient(to right, #fc4a1a, #f7b733);
  &:hover {
    transform: scale(1.2);
  }
}

  
</style>
<div>
    <center><button class="button">Click me!</button></center>
</div>
<div>
    <center><button class="special-button">No, click me!</button></center>
</div>
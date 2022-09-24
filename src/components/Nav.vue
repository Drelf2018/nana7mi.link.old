<template>
  <nav>
    <a href="/">🏠</a>
    <a :href="href" title="eyes">
      <img class="eyes" :src="src" alt="eyes">
    </a>
    <a href="/about">❔</a>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  props: {
    href: String,
    src: String
  }
}
</script>

<style>
nav {
  position: sticky;
  top: 0;
  padding: 0.5em;
  background-color: rgb(33, 37, 41);
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  z-index: 4;
}

.eyes {
  height: 40px;
  display: block;
  border-radius: 7px;
}
</style>
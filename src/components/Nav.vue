<template>
  <nav @click="ldd">
    <a href="/">🏠</a>
    <div id="island" @mouseleave="leave()">
      <span style="font-size: 75px; opacity: 0; transition: all 0.5s;">灵动岛</span>
    </div>
    <a :href="href">
      <img class="eyes" :src="src" alt="eyes" @mouseenter="enter()" >
    </a>
    <a href="/about">❔</a>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  props: {
    href: String,
    src: String,
    enter: Function,
    leave: Function
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

#island {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  margin: 0.5em auto;
  width: 95px;
  height: 40px;
  border-radius: 7px;
  transition: all 0.3s;
  background-color: #FFF;
  box-shadow: none;
  display: flex;
  justify-content: space-around;
  align-items: center;
  overflow: hidden;
  z-index: 5;
}

.ip14 {
  width: 265.5px;
  margin: 0 auto;
}

.eyes {
  position: relative;
  height: 40px;
  display: block;
  border-radius: 7px;
  z-index: 6;
}
</style>
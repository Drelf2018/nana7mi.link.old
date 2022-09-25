<template>
  <nav @click="ldd">
    <a href="/">🏠</a>
    <div id="island" @mouseleave="close"></div>
    <a :href="href" title="eyes">
      <img class="eyes" :src="src" alt="eyes" @mouseenter="open" >
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
  },
  mounted() {
    this.island = document.getElementById('island');
  },
  methods: {
    open() {
      this.island.style.width = "30%";
      this.island.style.boxShadow = "0 7px 10px grey";
      this.plan = setTimeout(() => {
        this.island.style.height = "40%";
      }, 300)
    },
    close() {
      if (this.plan) {
        clearInterval(this.plan);
        this.plan = null;
      }
      this.island.style.boxShadow = "none";
      this.island.style.width = "95px";
      this.island.style.height = "40px";
    }
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
  z-index: 5;
}

.eyes {
  position: relative;
  height: 40px;
  display: block;
  border-radius: 7px;
  z-index: 6;
}
</style>
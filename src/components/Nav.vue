<template>
  <nav @click="ldd">
    <a href="/">🏠</a>
    <div id="island" @mouseleave="close()">
      <img class="ip14" src="ip14.png">
    </div>
    <a :href="href">
      <img class="eyes" :src="src" alt="eyes" @mouseenter="open('265.5px', '265.5px', '535.7px', 0)" >
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
    open(w1="40%", w2="95%", h="40%", wait=300) {
      if (document.body.clientWidth > 883) this.island.style.width = w1;
      else this.island.style.width = w2;
      // this.island.lastChild.style.borderShadow = "0 7px 10px grey";
      this.plan = setTimeout(() => {
        this.island.style.height = h;
      }, wait)
    },
    close() {
      if (this.plan) {
        clearInterval(this.plan);
        this.plan = null;
      }
      // this.island.lastChild.style.borderShadow = "none";
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
  /* background-color: #FFF; */
  box-shadow: none;
  display: flex;
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
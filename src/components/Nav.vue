<template>
  <nav>
    <ion-icon class="menu" name="menu-outline" @click="move"></ion-icon>
    <div id="island" :class="status ? 'open' : 'close'" @mouseleave="status = 0">
      <div id="phone">
        <div style="height: 100%;display: flex;align-items: center;">
          <ion-icon name="logo-apple" class="github"></ion-icon>
          <p style="padding-top: 0.25em;">Dynamic Island</p>
        </div>
        <div class="link" style="height: 75%;width: auto;margin-right: 1em;padding-right: 0.5em;align-items: center;">
          <ion-icon name="logo-css3" class="github"></ion-icon>
          <div style="display: inline;">
            <a href="https://github.com/Drelf2018/nana7mi.link/blob/main/src/components/Nav.vue">
              Powered by <strong>CSS</strong>
            </a>
          </div>
        </div>
      </div>
      <div id="inner" style="z-index: 1;" :class="status ? 'inner-open' : 'inner-close'" v-html="inner"></div>
    </div>
    <a :href="href">
      <img class="eyes" :src="src" alt="eyes" @mouseenter="status = 1">
    </a>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  props: {
    href: String,
    src: String,
    move: Function,
    inner: String,
    status: Number
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
  z-index: 3;
}

.menu {
  left: 0.5em;
  top: 0.5em;
  position: fixed;
  color: #FFF;
  font-size: 1.8em;
  z-index: 4;
  transition: all 0.3s;
}

.menu:hover {
  opacity: 0.8;
}

#phone {
  position: absolute;
  display: flex;
  justify-content: space-between;
  align-items: center;
  top: 0;
  width: 100%;
  height: 45px;
  background-color: rgb(246, 248, 250);
  border-bottom: 3px solid rgb(33, 37, 41);
  transition: all 0.3s;
  z-index: 2;
}

#island {
  position: fixed;
  top: 0;
  margin: 0.5em auto;
  border-radius: 7px;
  background-color: #FFF;
  display: flex;
  justify-content: space-around;
  align-items: center;
  overflow: hidden;
  /* border: 1px solid #000; */
  z-index: 5;
}

.open {
  transition: width 0.3s ease 0s, height 0.3s ease 0.3s, box-shadow 0.3s ease 0s;
  width: 35%;
  height: 50%;
  box-shadow: 0 7px 10px grey;
}

.close {
  transition: all 0.3s;
  width: 95px;
  height: 40px;
  box-shadow: none;
}

#inner {
  position: relative;
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 100%;
  height: calc(100% - 48px);
  top: 24px;
}

.inner-open {
  transition: all 0.3s ease 0.3s;
  opacity: 1;
}

.inner-close {
  transition: all 0.3s;
  opacity: 0;
}

@media screen and (max-width: 900px) {
  .open {
    width: 95%;
  }
}

.eyes {
  position: relative;
  height: 40px;
  display: block;
  border-radius: 7px;
  z-index: 6;
}
</style>
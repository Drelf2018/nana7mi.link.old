<template>
  <nav>
    <ion-icon class="menu" name="menu-outline" @click="move"></ion-icon>
    <div id="island" @mouseleave="leave()">
      <div id="phone">
        <div style="height: 100%;display: flex;align-items: center;">
          <ion-icon name="logo-apple" id="github"></ion-icon>
          <p style="padding-top: 0.25em;">Dynamic Island</p>
        </div>
        <div class="link" style="height: 75%;width: auto;margin-right: 1em;padding-right: 0.5em;align-items: center;">
          <ion-icon name="logo-css3" id="github"></ion-icon>
          <div style="display: inline;">
            <a href="https://github.com/Drelf2018/nana7mi.link/blob/main/src/components/Nav.vue">
              Powered by <strong>CSS</strong>
            </a>
          </div>
        </div>
      </div>
      <div>
        <span style="font-size: 75px; opacity: 0; transition: all 0.5s;">灵动岛</span>
      </div>
    </div>
    <a :href="href">
      <img class="eyes" :src="src" alt="eyes" @mouseenter="enter()">
    </a>
    <!-- <a href="/about">❔</a> -->
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  props: {
    href: String,
    src: String,
    move: Function,
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
  transition: all 0.5s;
}

#island {
  position: fixed;
  top: 0;
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
  /* border: 1px solid #000; */
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
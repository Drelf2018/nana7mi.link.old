<template>
  <Nav href='https://t.bilibili.com/682043379459031137' src="src/assets/eyes.png"></Nav>
  <Swiper class="swiperBox" speed="7000" height="200px"></Swiper>
  <h1 id="title">
    😎 nana7mi.link
    <span style="font-size: 0.6em; color: grey"><em>{{ selected }}</em></span>
  </h1>
  <Rooms v-for="room in roomsRecently" :room="room"></Rooms>
</template>

<script>
import Nav from './components/nav.vue';
import Rooms from './components/Rooms.vue';
import Swiper from './components/Swiper.vue'


export default {
  name: 'App',
  components: {
    Nav,
    Rooms,
    Swiper
  },
  mounted() {
    var that = this;
    axios
      .get('https://api.nana7mi.link/rooms')
      .then((response) => that.rooms = response.data.rooms)
      .catch((error) => console.log(error));
  },
  data() {
    return {
      rooms: null,
      quotations: [
        '你们会无缘无故的说好用，就代表哪天无缘无故的就要骂难用',
        '哈咯哈咯，听得到吗',
        '还什么都没有更新，不要急好嘛',
        '直播只是工作吗直播只是工作吗直播只是工作吗？'
      ],
      timestamp: Date.parse(new Date()) / 1000
    }
  },
  computed: {
    selected() { return this.quotations[Math.floor((Math.random() * this.quotations.length))]; },
    roomsRecently() {
      if (this.rooms) return this.rooms.filter(room => this.timestamp - room.st <= 604800)
    }
  }
}
</script>

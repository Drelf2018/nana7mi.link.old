<template>
  <Nav href='https://t.bilibili.com/682043379459031137' src="eyes.png"></Nav>
  <div class="view">
    <Sider></Sider>
    <div class="main">
      <div class="sb">
        <Swiper speed="7000" height="200px" :banner="bannerFilter"></Swiper>
        <iframe src="//player.bilibili.com/player.html?aid=78090377&bvid=BV1vJ411B7ng&cid=133606284&page=1"
          scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
      </div>
      <h1 style="display: inline-block">
        😎 nana7mi.link
        <span style="font-size: 0.6em; color: grey"><em>{{ selected }}</em></span>
      </h1>
      <Rooms v-for="room in roomsRecently" :room="room"></Rooms>
    </div>
  </div>
</template>

<script>
import Nav from './components/nav.vue';
import Rooms from './components/Rooms.vue';
import Swiper from './components/Swiper.vue';
import Sider from './components/Sider.vue';


export default {
  name: 'App',
  components: {
    Nav,
    Rooms,
    Swiper,
    Sider
  },
  mounted() {
    var that = this;
    axios
      .get('https://api.nana7mi.link/rooms')
      .then(response => that.rooms = response.data.rooms)
      .catch(error => console.log(error));

    axios
      .get('https://api.nana7mi.link//api')
      .then(response => that.banner = response.data.data.banner)
      .catch(error => console.log(error));
  },
  data() {
    return {
      rooms: [],
      banner: [],
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
    roomsRecently() { return this.rooms.filter(room => this.timestamp - room.st <= 604800) },
    bannerFilter() {
      function Banner(link, url) {
        this.link = link;
        this.url = url;
        this.showInfo = function () {
          console.log(this.link + ': ' + this.url);
        }
      }
      var banner = this.banner.filter(b => b.location == "index_preview");
      var res = [new Banner("https://www.bilibili.com/video/BV1tG411g7Fo", "http://i0.hdslb.com/bfs/archive/b7868c38077aaa66e233499723a4d7490804f861.png")];
      for (var i = 0; i < banner.length; i++)
        res.push(new Banner(banner[i].link, banner[i].pic));
      res.push(res[0]);
      return res;
    }
  }
}
</script>

<style>
.main {
  width: 60%;
  margin: 20px auto;
  padding-left: 25%;
}

.sb {
  display: flex;
  justify-content: space-evenly;
  margin: 20px auto;
}

@media screen and (max-width: 900px) {
  .main {
    width: 75%;
    padding-left: 0;
  }
  .sb {
    display: none;
  }
}
</style>
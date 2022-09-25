<template>
  <Nav href='https://t.bilibili.com/682043379459031137' src="eyes.png"></Nav>
  <ion-icon class="menu" name="menu-outline" @click="moveSider"></ion-icon>
  <div class="view">
    <Sider id="sider" style="transition: all 0.5s"></Sider>
    <div id="main">
      <div class="sb">
        <Swiper speed="7000" height="200px" :banner="bannerFilter"></Swiper>
        <iframe class="roundShadow" src="//player.bilibili.com/player.html?aid=78090377&bvid=BV1vJ411B7ng&cid=133606284&page=1"
          scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
        <iframe class="roundShadow" src="//player.bilibili.com/player.html?aid=78090377&bvid=BV1pR4y1W7M7&cid=133606284&page=1"
          scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
      </div>
      <h1 id="title"><span @click="qtd++">😎</span> nana7mi.link</h1>
      <p id="subtitle"><strong><em>{{ selected }}</em></strong></p>
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
    this.sider = document.getElementById('sider');
    this.main = document.getElementById('main');
    var that = this;
    axios
      .get('https://api.nana7mi.link/rooms')
      .then(response => that.rooms = response.data.rooms)
      .catch(error => console.log(error));

    // axios
    //   .get('https://api.nana7mi.link/api')
    //   .then(response => that.banner = response.data.data.banner)
    //   .catch(error => console.log(error));
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
      qtd: 0,
      siderStatus: 1,
      siderMove: new Date().getTime(),
      timestamp: Date.parse(new Date()) / 1000
    }
  },
  computed: {
    selected() {
      return this.quotations[
        Math.floor(
          (Math.random() * this.quotations.length) + this.qtd
        ) - this.qtd
      ];
    },
    roomsRecently() { return this.rooms.filter(room => this.timestamp - room.st <= 604800) },
    bannerFilter() {
      function Banner(link, url) {
        this.link = link;
        this.url = url;
        this.showInfo = function () {
          console.log(this.link + ': ' + this.url);
        }
      }
      // var banner = this.banner.filter(b => b.location == "index_preview");
      var res = [
        new Banner(
          "https://www.bilibili.com/video/BV1tG411g7Fo",
          "http://i0.hdslb.com/bfs/archive/b7868c38077aaa66e233499723a4d7490804f861.png"
        ),
        new Banner(
          "https://www.bilibili.com/video/BV1pR4y1W7M7",
          "esu1.png"
        ),
        new Banner(
          "",
          "esu2.png"
        ),
        new Banner(
          "",
          "esu3.png"
        )
      ];
      // for (var i = 0; i < banner.length; i++)
      //   res.push(new Banner(banner[i].link, banner[i].pic));
      res.push(res[0]);
      return res;
    }
  },
  methods: {
    moveSider() {
      var tt = new Date().getTime();
      if (tt - this.siderMove > 505) this.siderMove = tt;
      else return;
      this.siderStatus ^= 1;
      this.main.style.paddingLeft = this.siderStatus *  20 + "%";
      if (this.sider.offsetWidth / document.body.clientWidth < 0.3) {
        if (this.siderStatus == 1) {
          this.sider.style.transition = "none";
          this.sider.style.left =  "-20%";
          setTimeout(() => {
            this.sider.style.transition = "all 0.5s";
            this.sider.style.left =  "0%";
          }, 30)
        } else {
          this.sider.style.left = "-20%";
          setTimeout(() => {
            this.sider.style.transition = "none";
            this.sider.style.left = "-100%";
          }, 500)
        }
      } else {
        this.sider.style.transition = "all 0.5s";
        this.sider.style.left = (this.siderStatus ^ 1) * -100 + "%";
      }
    }
  }
}
</script>

<style>
.menu {
  left: 0.5em;
  top: 0.5em;
  position: fixed;
  color: #F5F5F7;
  font-size: 1.8em;
  z-index: 6;
  transition: all 0.3s;
}

.menu:hover {
  opacity: 0.8;
}

.view {
  margin: 0;
  padding: 0;
}

#title {
  display: inline-block;
}

#subtitle {
  display: inline-block;
  padding-left: 0.5em;
  font-size: 1em;
  color: grey;
}

#main {
  width: 75%;
  margin: 0px auto;
  padding-left: 20%;
  transition: all 0.5s;
}

.roundShadow {
  border-radius: 10px;
  box-shadow: 0 7px 10px rgb(100, 100, 100);
}

.sb {
  display: flex;
  justify-content: space-between;
  margin: 20px auto;
}

@media screen and (max-width: 900px) {
  #title {
    display: block;
    margin: 0.2em 0;
  }

  #subtitle {
    display: block;
    padding-bottom: 0.2em;
  }

  #main {
    width: 75%;
    padding-left: 0;
  }
  .sb {
    display: none;
  }
}
</style>
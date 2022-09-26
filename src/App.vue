<template>
  <Nav href='https://t.bilibili.com/682043379459031137' src="eyes.png" :enter="open" :leave="close"></Nav>
  <ion-icon class="menu" name="menu-outline" @click="move"></ion-icon>
  <div class="view">
    <Sider id="sider" style="transition: all 0.5s" :callback="roomClick"></Sider>
    <div id="main">
      <div class="gallery">
        <Swiper speed="7000" height="200px" :banner="bannerFilter"></Swiper>
        <iframe class="roundShadow"
          src="//player.bilibili.com/player.html?aid=78090377&bvid=BV1vJ411B7ng&cid=133606284&page=1" scrolling="no"
          frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
        <iframe class="roundShadow"
          src="//player.bilibili.com/player.html?aid=78090377&bvid=BV1pR4y1W7M7&cid=133606284&page=1" scrolling="no"
          frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
      </div>
      <h1 id="title" onselectstart="return false;"><span @click="qtd++">😎</span> nana7mi.link</h1>
      <p id="subtitle"><strong><em>{{ selected }}</em></strong></p>
      <input id="roomid" type="text" placeholder="支持模糊搜索及直播间号精确定位"
        @input="event => {this.selectName = event.target.value; this.danmaku = null;}" @keyup.enter.native="event => roomClick(event.target.value, true)">
      <Room v-for="room in roomsRecently" style="opacity: 0;left: 100%;" :id="room.room + '_' + room.st" :room="room"
        @click="roomClick(room)"></Room>
      <Danmaku :danmaku="danmaku"></Danmaku>
    </div>
  </div>
</template>

<script>
import Nav from './components/nav.vue';
import Room from './components/Room.vue';
import Swiper from './components/Swiper.vue';
import Sider from './components/Sider.vue';
import Danmaku from './components/Danmaku.vue';


export default {
  name: 'App',
  components: {
    Nav,
    Room,
    Swiper,
    Sider,
    Danmaku
},
  mounted() {
    this.sider = document.getElementById('sider');
    this.main = document.getElementById('main');
    this.island = document.getElementById('island');
    axios
      .get('https://api.nana7mi.link/rooms')
      .then(response => { this.rooms = response.data.rooms; this.subroom = false; this.allRooms = this.rooms; })
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
      qtd: 0,
      selectName: null,
      siderStatus: 0,
      move: this.throttle(this.moveSider, 500),
      subroom: false,
      timestamp: Date.parse(new Date()) / 1000,
      danmaku: null
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
    roomsRecently() {
      if (!this.selectName)
        return this.rooms.filter(room => this.subroom || (this.timestamp - room.st <= 604800))
      else {
        this.subroom = false;
        return this.allRooms.filter(room => room.username.includes(this.selectName)
          || room.room.toString().includes(this.selectName)
          || room.uid.toString().includes(this.selectName)
        )
      }
    },
    bannerFilter() {
      function Banner(link, url) {
        this.link = link;
        this.url = url;
      };
      var res = [
        new Banner(
          "https://www.bilibili.com/video/BV1tG411g7Fo",
          "http://i0.hdslb.com/bfs/archive/b7868c38077aaa66e233499723a4d7490804f861.png"
        ),
        new Banner("https://www.bilibili.com/video/BV1pR4y1W7M7", "esu1.png"),
        new Banner("", "esu2.png"),
        new Banner("", "esu3.png")
      ];
      res.push(res[0]);
      return res;
    }
  },
  methods: {
    open(inner = null, w1 = "25%", w2 = "95%", h = "30%", wait = 300) {
      if (inner) {
        this.island.innerHTML = inner;
        this.island.lastChild.style.opacity = 0;
        this.island.lastChild.style.transition = "all 0.5s";
      }
      if (document.body.clientWidth > 883) this.island.style.width = w1;
      else this.island.style.width = w2;
      this.island.style.boxShadow = "0 7px 10px grey";
      this.plan = setTimeout(() => {
        this.island.style.height = h;
        this.island.lastChild.style.opacity = 1;
      }, wait)
    },
    close() {
      if (this.plan) {
        clearInterval(this.plan);
        this.plan = null;
      }
      this.island.style.boxShadow = "none";
      this.island.style.width = "95px";
      this.island.style.height = "40px";
      this.island.lastChild.style.opacity = 0;
    },
    updateRooms(newRooms=null, fn=null, after_fn=null) {
      var rooms = document.getElementsByClassName("live")
      Array.from(rooms).forEach(
        (pp) => {
          pp.style.opacity = 0;
          pp.style.left = "100%";
        }
      )
      if (newRooms) setTimeout(() => {
        if (fn) fn();
        this.rooms = newRooms;
        if (after_fn) setTimeout(after_fn, 500);
      }, 500);
    },
    roomClick(roomid, force = false) {
      if (this.subroom && !force) {
        if (this.rooms.length == 1 && this.rooms[0] == roomid) return;
        this.updateRooms([roomid])
        axios
          .get('https://api.nana7mi.link/live/' + roomid.room + "/" + roomid.index)
          .then(response => response.data.live.danmaku)
          .then(danmaku => {
            if (!danmaku) return;
            this.danmaku = danmaku
          })
      } else {
        if (!parseInt(roomid))
          if (parseInt(roomid.room)) roomid = roomid.room
          else return
        axios
          .get('https://api.nana7mi.link/live/' + roomid)
          .then(response => response.data.lives)
          .then(lives => {
            if (!lives) {
              this.open('<span style="font-size: 50px">房间号不存在</span>');
              setTimeout(this.close, 3000);
            } else {
              var total = lives.length;
              lives.forEach((value, index, arr) => value.index = total - index - 1);
              this.updateRooms(
                lives,
                () => { this.selectName = null; this.subroom = true; },
                () => document.getElementById('roomid').scrollIntoView({ behavior: 'smooth' })
              )
            }
          })
          .catch(error => console.log(error));
      }
    },
    moveSider() {
      this.siderStatus ^= 1;
      this.main.style.paddingLeft = this.siderStatus * 20 + "%";
      if (this.sider.offsetWidth / document.body.clientWidth < 0.3) {
        if (this.siderStatus == 1) {
          this.sider.style.transition = "none";
          this.sider.style.left = "-20%";
          setTimeout(() => {
            this.sider.style.transition = "all 0.5s";
            this.sider.style.left = "0%";
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
  color: #FFF;
  font-size: 1.8em;
  z-index: 4;
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
  margin-top: 1.44px;
  display: inline-block;
}

#subtitle {
  display: inline-block;
  padding-left: 0.5em;
  font-size: 1em;
  color: grey;
}

#roomid {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: 2.5em;
  font-size: 1em;
  font-weight: 540;
  padding: 1px 0 0 0.5em;
  margin: 0 auto 1.34em;
  border: 1px solid #ced4da;
  border-radius: 0.5em;
  transition: all 0.2s;
}

#roomid:focus {
  border-color: #86b7fe;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgb(13 110 253 / 25%);
}

#main {
  width: 75%;
  margin: 0px auto;
  transition: all 0.5s;
}

.roundShadow {
  border-radius: 10px;
  box-shadow: 0 7px 10px rgb(100, 100, 100);
}

.gallery {
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

  .gallery {
    display: none;
  }
}
</style>
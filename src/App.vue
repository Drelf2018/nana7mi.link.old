<template>
  <a id="top"></a>
  <Nav href='https://t.bilibili.com/682043379459031137' src="eyes.png" :move="move" :inner="inner" :status="navStatus"></Nav>
  <div class="view">
    <Sider id="sider" :status="siderStatus"></Sider>
    <div id="main" :style="'padding-left: ' + siderStatus * 20 + '%;'">
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
        @input="event => {this.selectName = event.target.value; this.danmaku = null;}"
        @keyup.enter.native="event => roomClick(event.target.value, true)">
      <Room v-for="room in roomsRecently" style="opacity: 0;left: 100%;" :id="room.room + '_' + room.st" :room="room"
        @click="roomClick(room)"></Room>
      <Danmaku :danmaku="danmaku"></Danmaku>
    </div>
  </div>
</template>

<script>
import Nav from './components/Nav.vue';
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
      inner: '<span style="font-size: 75px; opacity: 1; transition: all 0.5s;">灵动岛</span>',
      navStatus: 0,
      move: this.throttle(() => this.siderStatus ^= 1, 500),
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
        if (this.subroom) return this.rooms
        else return this.rooms.filter(room =>  this.timestamp - room.st <= 604800)
      else {
        this.subroom = false;
        return this.allRooms.filter(room => room.username.includes(this.selectName)
            || room.room.toString().includes(this.selectName)
            || room.uid.toString().includes(this.selectName)
            || room.title.includes(this.selectName)
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
          "https://i0.hdslb.com/bfs/archive/b7868c38077aaa66e233499723a4d7490804f861.png"
        ),
        new Banner(
          "https://www.bilibili.com/video/BV1T24y1R7wd",
          "http://i1.hdslb.com/bfs/archive/ab9738d7aee96044183b61c7dd9c95eb1ec17ed1.jpg"
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
    updateRooms(newRooms=null, beforeFn=null, immediatelyFn=null, afterFn=null) {
      var rooms = document.getElementsByClassName("live")
      Array.from(rooms).forEach(
        (pp) => {
          pp.style.opacity = 0;
          pp.style.left = "100%";
        }
      )
      if (beforeFn) beforeFn();
      if (newRooms) setTimeout(() => {
        this.rooms = newRooms;
        if (immediatelyFn) immediatelyFn();
        if (afterFn) setTimeout(afterFn, 500);
      }, 500);
    },
    roomClick(roomid, force = false) {
      if (this.subroom && !force) {
        if (this.rooms.length == 1 && this.rooms[0] == roomid) return;
        this.updateRooms([roomid],
          () => document.getElementById('top').scrollIntoView({ behavior: 'smooth' }),
          () => {
            axios
              .get('https://api.nana7mi.link/live/' + roomid.room + "/" + roomid.index)
              .then(response => this.danmaku = response.data.live.danmaku)
          }, null)
      } else {
        if (!parseInt(roomid))
          if (parseInt(roomid.room)) roomid = roomid.room
          else return
        axios
          .get('https://api.nana7mi.link/live/' + roomid)
          .then(response => response.data.lives)
          .then(lives => {
            if (!lives) {
              this.inner = '<span style="font-size: 50px">房间号不存在</span>';
              this.navStatus = 1;
              setTimeout(() => this.navStatus = 0, 3000);
            } else {
              var total = lives.length;
              lives.forEach((value, index, arr) => value.index = total - index - 1);
              this.updateRooms(
                lives,
                null,
                () => { this.selectName = null; this.subroom = true; },
                () => document.getElementById('roomid').scrollIntoView({ behavior: 'smooth' })
              )
            }
          })
          .catch(error => console.log(error));
      }
    }
  }
}
</script>

<style>
.view {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
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
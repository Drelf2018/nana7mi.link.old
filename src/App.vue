<template>
  <Nav href='https://t.bilibili.com/682043379459031137' src="eyes.png" :move="move" :inner="inner" :status="navStatus"></Nav>
  <div class="view">
    <Sider id="sider" :status="siderStatus"></Sider>
    <div id="main" :style="'padding-left: ' + siderStatus * 20 + '%;'">
      <div style="display: flex;margin-top: 1em;justify-content: space-between">
        <div class="show-block" style="width: 100%;">
          <h1 id="title" onselectstart="return false;"><span @click="qtd++">😎</span> nana7mi.link</h1>
          <p id="subtitle"><strong><em>{{ selected }}</em></strong></p>
          <input id="roomid" type="text" placeholder="支持模糊搜索及直播间号精确定位"
            @input="event => {this.selectName = event.target.value; this.danmaku = null; this.button[3].maxPrice = ''; this.button[4].content = '';}"
            @keyup.enter.native="event => roomClick(event.target.value, true)">
          <!-- 目前可用指令：esu -->
          
          <div class="controler" :style="danmaku ? 'opacity: 1;' : 'opacity: 0;'">
            <div :class="[btn.status ? 'down' : 'up', 'link', 'selector']" v-for="btn in (danmaku ? button.slice(0, 3) : [])" @click="btn.status ^= 1">
              <div style="display: inline;">
                <strong>{{ btn.name }}</strong><br />
                <span style="color: grey;">{{ btn.status ? '是' : '否'}}</span>
              </div>
            </div>
          </div>
          <div class="controler" :style="'align-items: center;' + (danmaku ? 'opacity: 1;' : 'opacity: 0;')">
            <input v-if="danmaku" v-model="button[3].maxPrice" type="number" style="width: 48%;margin: 0px;" placeholder="大于等于指定金额，不填默认为零。">
            <input v-if="danmaku" @keyup.enter.native="queryHelp" type="text" style="width: 48%;margin: 0px;" placeholder="内容筛选，高阶用法输入 /help 查看。">
          </div>
        </div>
        <div class="show-block" id="gallery" style="margin-left: 1em;">
          <Swiper speed=7000 height="229px" :banner="bannerFilter"></Swiper>
        </div>
      </div>
      <Room v-for="room in roomsRecently" style="opacity: 0;left: 100%;" :id="room.room + '_' + room.st" :room="room"
        @click="roomClick(room)"></Room>
      <Danmaku :danmaku="danmaku" :button="button"></Danmaku>
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
      innerPlan: null,
      navStatus: 0,
      move: this.throttle(() => this.siderStatus ^= 1, 500),
      subroom: false,
      timestamp: Date.parse(new Date()) / 1000,
      danmaku: null,
      button: [
        {name: '礼物', status: 0},
        {name: '大航海', status: 0},
        {name: '醒目留言', status: 0},
        {maxPrice: null, status: 0},
        {content: null},
        {mountedWait: 0}
      ]
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
        else return this.rooms.filter(room => this.timestamp - room.st <= 604800)
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
    queryHelp(event) {
      if (event.target.value != '/help')
        this.button[4].content = event.target.value
      else {
        this.inner = '<span style="font-size: 25px;padding: 1em">用类似逻辑电路的格式约定搜索方式，例如：\
          A B+C D 表示搜索同时包含 A 与 D 且包含 B 或 C 。\
          即空格表示与、加号表示或。</span>';
        this.navStatus = 1;
        setTimeout(() => this.navStatus = 0, 10000);
      }
    },
    updateRooms(newRooms = null, immediatelyFn = null) {
      var rooms = document.getElementsByClassName("live")
      Array.from(rooms).forEach(
        (pp) => {
          pp.style.opacity = 0;
          pp.style.left = "100%";
        }
      )
      if (newRooms) setTimeout(() => {
        this.rooms = newRooms;
        if (immediatelyFn) immediatelyFn();
      }, 500);
    },
    roomClick(roomid, force = false) {
      if (this.subroom && !force) {
        if (this.rooms.length == 1 && this.rooms[0] == roomid) {
          if (this.button[5].mountedWait) {roomid = roomid.room; this.button[5].mountedWait=0;}
          else return
        }
        else {
          this.updateRooms([roomid], () => {
            axios
              .get('https://api.nana7mi.link/live/' + roomid.room + "/" + roomid.index)
              .then(response => this.danmaku = response.data.live.danmaku)
          })
          return;
        }
      }

      this.danmaku = null;
      if (!parseInt(roomid))
        if (parseInt(roomid.room)) roomid = roomid.room
        else {
          switch (roomid) {
            case "esu":
              this.inner = '<iframe class="roundShadow" width=95% height=90% src="//player.bilibili.com/player.html?aid=78090377&bvid=BV1pR4y1W7M7&cid=133606284&page=1" scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>';
              break;
            case "/user":
              var inp = document.getElementById("roomid");
              inp.placeholder = "输入被查询人 UID";
              inp.value = '';
              return
            default:
              return;
          }
          clearInterval(this.innerPlan);
          this.navStatus = 1;
          this.innerPlan = setTimeout(() => this.navStatus = 0, 3000);
        }
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
            this.updateRooms(lives, () => { this.selectName = null; this.subroom = true; })
          }
        })
        .catch(error => console.log(error));
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

input {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: 2.5em;
  font-size: 1em;
  font-weight: 540;
  padding: 1px 0 0 0.5em;
  margin: 0 auto;
  border: 1px solid #ced4da;
  border-radius: 0.5em;
  transition: all 0.2s;
}

input:focus {
  border-color: #86b7fe;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgb(13 110 253 / 25%);
}

.controler {
    position: relative;
    margin-top: 1em;
    display: flex;
    justify-content: space-between;
    transition: all 0.5s;
}

.selector {
    padding: 0.3em 0 0.3em 1em;
    width: 25%;
    background-color: #FFF;
}

.up {
    background-color: #FFF;
}

.down {
    background-color: hsl(196, 100%, 97%);
    box-shadow: 0 1.5px 4px skyblue;
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

  #gallery {
    display: none;
  }
}
</style>
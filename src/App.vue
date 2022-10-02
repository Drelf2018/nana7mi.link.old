<template>
  <a id="top"></a>
  <Nav href='https://t.bilibili.com/682043379459031137' 
    src="https://i0.hdslb.com/bfs/new_dyn/0de10012b4a96d7d4bcd82728f77b2051464240042.png" 
    :move="move" :inner="inner" :status="navStatus">
  </Nav>
  <div class="view">
    <Sider id="sider" :status="siderStatus"></Sider>
    <div id="main" :style="'padding-left: ' + siderStatus * 20 + '%;'">
      <div style="display: flex;margin-top: 1em;justify-content: space-between">
        <div class="show-block" style="width: 100%;">
          <h1 id="title" onselectstart="return false;">
            <span @click="this.qid = Math.floor((Math.random() * this.quotations.length))">😎 </span> 
            <a href="/">nana7mi.link</a>
          </h1>
          <p id="subtitle"><strong><em>{{ this.quotations[this.qid] }}</em></strong></p>
          <input id="roomid" type="text" placeholder="支持模糊搜索及直播间号精确定位"
            @input="queryLiver" @keyup.enter.native="event => roomClick(event.target.value)">
          <!-- 目前可用指令：esu user -->
          
          <div class="controler" :style="danmaku ? 'opacity: 1;' : 'opacity: 0;'">
            <div :class="[btn.status ? 'down' : 'up', 'link', 'selector']" v-for="(btn, index) in (danmaku ? button.slice(0, 3) : [])" @click="btn.status ^= 1">
              <div style="display: inline;">
                <strong>{{ btn.name }}</strong>
                <span style="color: red;">￥{{ 
                  index == 0 ? this.rooms[0].send_gift.toFixed(2) :
                  index == 1 ? this.rooms[0].guard_buy.toFixed(2) :
                  index == 2 ? this.rooms[0].super_chat_message.toFixed(2) : "0.00"
                }}</span><br />
                <span style="color: grey;">{{ btn.status ? '是' : '否'}}</span>
              </div>
            </div>
          </div>
          <div class="controler" :style="'align-items: center;' + (danmaku ? 'opacity: 1;' : 'opacity: 0;')">
            <input class="inp" v-if="danmaku" v-model="button[3].maxPrice" type="number" placeholder="金额筛选，默认不小于零。">
            <input class="inp" v-if="danmaku" @input="queryHelp" @keyup.enter.native="queryHelp" type="text" placeholder="内容筛选，输入 /help 查看更多。">
          </div>
        </div>
        <div class="show-block" id="gallery" style="margin-left: 1em;">
          <Swiper speed=5000 height="229px" :banner="banner"></Swiper>
        </div>
      </div>
      <div v-for="live in liveList">
        <Room v-for="room in live.rooms" style="opacity: 0;left: 100%;" :id="room.room + '_' + room.st" :room="room"
          @click="roomClick(room)"></Room>
        <Danmaku :danmaku="live.danmaku" :button="button" :index="live.index" :id="'danmaku' + (live.index ? live.index : '')"></Danmaku>
      </div>
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
    this.queryUser = null;
    this.get("rooms", data => {
      this.allRooms = data.rooms;
      this.allRooms.forEach(room => room.status = 1);
      this.rooms = this.allRooms;
    });
  },
  data() {
    return {
      rooms: [],
      allRooms: [],
      quotations: [
        '你们会无缘无故的说好用，就代表哪天无缘无故的就要骂难用',
        '哈咯哈咯，听得到吗',
        '还什么都没有更新，不要急好嘛',
        '直播只是工作吗直播只是工作吗直播只是工作吗？'
      ],
      qid: 0,
      selectName: null,
      siderStatus: 0,
      inner: '<span style="font-size: 75px; opacity: 1; transition: all 0.5s;">灵动岛</span>',
      innerPlan: null,
      navStatus: 0,
      move: this.throttle(() => this.siderStatus ^= 1, 500),
      danmaku: null,
      button: [
        {name: '礼物', status: 0},
        {name: '大航海', status: 0},
        {name: '醒目留言', status: 0},
        {maxPrice: null, status: 0},
        {content: null},
        {mountedWait: 0},
        {timeStr: null, dateStr: null, baseStr: null}
      ],
      queryLiver: this.debounce(event => {
        if (!this.queryUser) {
          this.selectName = event.target.value;
          this.danmaku = null;
          this.button[3].maxPrice = '';
          this.button[4].content = '';
        }
      }, 300),
      queryHelp: this.debounce(event => {
        if (event.target.value != '/help')
          this.button[4].content = event.target.value
        else {
          this.inner = '<span style="font-size: 25px;padding: 1em">用类似逻辑电路的格式约定搜索方式，例如：\
            A B+C D 表示搜索同时包含 A 与 D 且包含 B 或 C 。\
            即空格表示与、加号表示或。</span>';
          this.navStatus = 1;
          setTimeout(() => this.navStatus = 0, 10000);
        }
      }),
      queryUser: null,
      queryRunning: false,
      userDanmaku: []
    }
  },
  computed: {
    liveList() {
      if (!this.queryUser) return [{rooms: this.roomsSelected, danmaku: this.danmaku}]
      else return this.userDanmaku
    },
    roomsSelected() {
      if (!this.selectName) return this.rooms
      else return this.allRooms.filter(
        room => room.title.includes(this.selectName)
             || room.username.includes(this.selectName)
             || room.uid.toString().includes(this.selectName)
             || room.room.toString().includes(this.selectName))
    },
    banner() {
      function Banner(link, url) {
        this.link = link;
        this.url = url;
      };
      var res = [
        new Banner(
          "https://www.bilibili.com/video/BV1vJ411B7ng",
          "https://i2.hdslb.com/bfs/archive/7fe8272ef4c90d07ba2dba968638392f8d5bf490.jpg"
        ),    
        new Banner(
          "https://www.bilibili.com/video/BV1he4y1r79x",
          "https://i1.hdslb.com/bfs/archive/ca796b3fe2a213c652ebb32469d81511036c7117.jpg"
        ),
        new Banner(
          "https://www.bilibili.com/video/BV1tG411g7Fo",
          "https://i0.hdslb.com/bfs/archive/b7868c38077aaa66e233499723a4d7490804f861.png"
        ),
        new Banner(
          "https://www.bilibili.com/video/BV1T24y1R7wd",
          "https://i1.hdslb.com/bfs/archive/ab9738d7aee96044183b61c7dd9c95eb1ec17ed1.jpg"
        ),
        new Banner(
          "https://www.bilibili.com/video/BV1pR4y1W7M7",
          "https://i0.hdslb.com/bfs/new_dyn/8b90b7582c6fa3023eda3ffb58bf8eeb1464240042.png"
        ),
        new Banner("", "https://i0.hdslb.com/bfs/new_dyn/3c611630235bca6cc7eadca431573c1f1464240042.png")
      ];
      res.push(res[0]);
      return res;
    }
  },
  methods: {
    get(url, fn=null) {
      axios
        .get('https://api.nana7mi.link/'+url)
        .then(response => {
          if(response.data) 
            if (fn) fn.call(this, response.data)
        })
        .catch(error => console.log(error));
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
    command(cmd) {
      switch (cmd) {
        case "esu":
          this.inner = '<iframe class="roundShadow" width=95% height=90% src="//player.bilibili.com/player.html?aid=78090377&bvid=BV1pR4y1W7M7&cid=133606284&page=1" scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>';
          break;
        case "user":
          var inp = document.getElementById("roomid");
          inp.placeholder = "输入被查询人 UID";
          inp.value = '';
          if (!this.rooms[0].sp) clearInterval(this.rooms[0].plan)
          this.queryUser = function(uid) {
            if (!parseInt(uid)) return;
            if (this.queryRunning) return;
            this.queryRunning = true
            this.get("uid/"+uid, data=>{
              this.danmaku = null
              this.userDanmaku = []
              var tempDanmaku = []
              var index = 1
              data.danmaku.forEach(dm => {
                if (!dm.room_info){
                  if (String(dm.time).length > 10) dm.time /= 1000
                  tempDanmaku.push(dm)
                }
                else {
                  if (tempDanmaku.length) {
                    this.userDanmaku.push({rooms: [], danmaku: tempDanmaku, index: index})
                    tempDanmaku = []
                    index += 1
                  }
                  this.userDanmaku.push({rooms: [dm.room_info], danmaku: dm.danmaku, index: index})
                  index += 1
                }
              })
              if (tempDanmaku.length) this.userDanmaku.push({rooms: [], danmaku: tempDanmaku, index: index})
              this.queryRunning = false
            })
          }
          return
        case "/error":
          this.inner = '<span style="font-size: 50px">我不会<br />长大以后再学习</span>';
          break
        default:
          return;
      }
      clearInterval(this.innerPlan);
      this.navStatus = 1;
      this.innerPlan = setTimeout(() => this.navStatus = 0, 3000);
    },
    getLives(roomid) {
      // 选择具体主播或者返回时搜索
      this.danmaku = null;
      this.get("live/"+roomid, data => {
        if (data.status) {
          this.inner = '<span style="font-size: 50px">' + data.status + '</span>';
          this.navStatus = 1;
          setTimeout(() => this.navStatus = 0, 3000);
        } else {
          var lives = data.lives;
          var total = lives.length;
          lives.forEach((value, index, arr) => {value.index = total - index - 1; value.status = 2;});
          this.updateRooms(lives, () => {
            this.selectName = null;
            setTimeout(()=>document.getElementById('top').scrollIntoView({ behavior: 'smooth' }), 500);
          })
        }
      })
    },
    roomClick(room) {
      if (this.queryUser) this.queryUser(room)
      else if (parseInt(room)) this.getLives(room)
      else if (room.status == 2) { // 查看具体弹幕
        room.status = 3;
        this.button[6].dateStr = new Date(room.st * 1000).Format('yyyy-MM-dd')
        this.button[6].baseStr = new Date(room.st * 1000).Format('hh:mm:ss')
        this.updateRooms([room], () => {
          this.get("live/" + room.room + "/" + room.index, data => {
            var new_room = data.live;
            new_room.status = 3;
            new_room.sp = room.sp;
            if (!room.sp) new_room.plan = setInterval(() => {
              this.get("live/" + room.room + "/" + room.index, data => this.danmaku = data.live.danmaku)
            }, 11000)
            this.rooms = [new_room]
            this.danmaku = new_room.danmaku
          })
        })
      }
      else if (room.status == 3 && this.button[5].mountedWait) { // 返回选择
        if (!room.sp) clearInterval(room.plan)
        this.button[5].mountedWait = 0;
        this.getLives(room.room);
      }
      else if (room.status == 1) this.getLives(room.room)
      else this.command(room)
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
    width: 30%;
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

.inp {
  width: 49%;
  margin: 0px;
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

  .controler{
    flex-direction: column;
    align-items: center;
  }

  .selector {
    width: 95%;
    margin-bottom: 0.5em;
  }

  .inp {
    width: 100%;
    margin-bottom: 0.5em;
  }
}
</style>
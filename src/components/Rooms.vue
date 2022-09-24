<template>
    <div class="live">
        <a :href="'https://space.bilibili.com/' + room.uid">
            <img class="cover" :alt="room.cover" :src="room.cover ? room.cover : noCover">
        </a>
        <div class="info">
            <a :href="'https://space.bilibili.com/' + room.uid" style="color: #000"><strong>{{ room.username }}</strong></a>
            <a v-show="!room.sp" class="living" :href="'https://live.bilibili.com/' + room.room">直播中</a>
            <div class="data">
                <div class="column" v-for="(value, key) in info">
                    <p class="time">{{ key }}</p>
                    <strong>{{ value }}</strong>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Rooms',
    props: {
        room: Object
    },
    methods: {
        format(tt) {
            if (tt) return new Date(tt * 1000).Format("yyyy-MM-dd hh:mm:ss");
            else return '直播中';
        }
    },
    data() {
        return {
            noCover: 'https://i0.hdslb.com/bfs/live/new_room_cover/cdc675883ef54f3ed1a8ceacc638fcd145ef3bbb.jpg'
        }
    },
    computed: {
        info() {
            return {
                '标题': this.room.title,
                '开始': this.format(this.room.st),
                '结束': this.format(this.room.sp),
                '营收': (this.room.guard_buy + this.room.send_gift + this.room.super_chat_message).toFixed(2)
            }
        }
    }
}
</script>

<style>
.living {
    color: #FFF;
    font-weight: 700;
    margin-left: 0.5em;
    padding: 0.3em 0.4em;
    border-radius: 0.25em;
    background-color: rgb(13, 110, 253);
}

.cover {
    width: 196px;
    height: 110px;
    float: left;
    margin: 20px;
    border-radius: 10px;
    box-shadow: 0 7px 10px grey;
    transition: all 0.3s;
}

.cover:hover {
    opacity: 0.7;
}

.live {
    /* margin: 0px 15%; */
    overflow: hidden;
}

.time {
    color: grey;
}

/* 创建四个相等的列 */
.column {
    float: left;
    width: 25%;
}

.data {
    display: flex;
}

.info {
    margin-top: 26px;
}

/* 响应式布局 - 小于 600 px 时改为上下布局 */
@media screen and (max-width: 900px) {
    .time {
        display: inline-block;
        margin: 0.5em 0.5em 0 0;
    }

    .column {
        width: 100%;
    }

    .data {
        flex-direction: column;
    }

    .cover {
        float: none;
    }

    .info {
        margin-top: 0px;
        margin-left: 20px;
        margin-bottom: 10px;
    }
}
</style>
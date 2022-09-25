<template>
    <div class="hidden-sider" style="left: 0%">
        <div style="overflow: auto; height: 100%">
            <p style="font-size: 50px">你好李鑫</p>
            <p style="font-size: 50px">这个颜色叫</p>
            <p style="font-size: 100px">Aqua</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Sider',
    data() {
        return {
            timer: null,
            count: 0,
            swiper: null,
            lsatMove: new Date().getTime()
        }
    }
}
</script>

<style>
.hidden-sider {
    top: 56px;
    width: 20%;
    height: calc(100vh - 56px);
    position: fixed;
    background-color: aqua;
}

@media screen and (max-width: 900px) {
  .hidden-sider {
    width: 100%;
  }
}
</style>

<template>
    <div id="test">
        <div style="overflow: auto; height: 100%">
            <p style="font-size: 100px">你好</p>
            <p style="font-size: 100px">你好</p>
            <p style="font-size: 100px">你好</p>
            <p style="font-size: 100px">你好</p>
            <p style="font-size: 100px">你好</p>
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
#test {
    top: 56px;
    width: 25%;
    height: calc(100vh - 56px);
    position: fixed;
    background-color: aqua;
}

@media screen and (max-width: 900px) {
  #test {
    display: none;
  }
}
</style>

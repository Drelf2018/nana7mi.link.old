<template>
    <div class="hidden-sider" style="left: -100%">
        <div style="overflow: auto; height: 100%">
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
    background-color: #FFF;
    border-right: 1px solid rgb(216, 222, 228);
    z-index: 4;
}

@media screen and (max-width: 900px) {
  .hidden-sider {
    width: 100%;
  }
}
</style>

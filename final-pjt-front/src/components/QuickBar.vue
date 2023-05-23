<template>
    <div class="container">
        <div class="row">
            <router-link class="col-12 link" to="mapview/"><div class="box">근처은행 검색</div></router-link>
            <router-link class="col-12 link" to="wordsearch/"><div class="box">백과사전 검색</div></router-link>
            <router-link class="col-12 link" to="mapview/"><div class="box">다른게 뭔가</div></router-link>
            <router-link class="col-12 link" to="mapview/"><div class="box">더 있을까요?</div></router-link>
            <router-link class="col-12 link" to="mapview/"><div class="box"> 암거나 넣으면</div></router-link>
            <router-link class="col-12 link" to="mapview/"><div class="box">될것 같은데요</div></router-link>
        </div>
    </div>
</template>

<script>
export default {
name: 'QuickBar.vue',
}
</script>

<style>
    .box {
    font-size: 15px;
    width: 100%;
    height: 4rem;
    background-color: powderblue;
    }
    .link {
    text-decoration-line: none;
    color: black;
    }
</style>

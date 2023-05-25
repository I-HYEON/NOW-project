<template>
  <div class="container">
    
    <div class="row justify-content-center">
      <div class="col-md-8">
        <br>
        
        <h4 class="text-center">가까운 은행을 검색해보세요</h4>
        <div>
          <input type="text" @keyup.enter="search" placeholder="찾으시는 은행명 혹은 지역명을 입력하세요" v-model="searchKeyword" style="width:90%;">
          <button type="button" @click="search"  style="margin-top:1px; margin-left:7px" class="btn btn-outline-success btn-sm">검색</button>

        </div>
      </div>
    </div>
    <div class="row justify-content-center mt-4">
      <div >
        <div id="map" class="map-container"></div>
      </div>
    </div>
    <div class="row justify-content-center mt-4" v-if="bankList.length">
      <div>
        <p>근처에 총 {{ bankList.length }} 개의 은행이 있습니다.</p>
        <hr>
        <div v-for="(bank, index) in bankList" :key="bank.id">
          <ul>
            <li style="list-style-type: none;">{{ index + 1 }}번째 은행</li>
            <li>{{ bank.place_name }}</li>
            <li>{{ bank.category_name }}</li>
            <li v-if="bank.phone">{{ bank.phone }}</li>
            <li v-if="bank.road_address_name">{{ bank.road_address_name }}</li>
            <li><a :href="bank.place_url">{{ bank.place_url }}</a></li>
          </ul>
          <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { BIconBoundingBox } from 'bootstrap-vue';


export default {
  name: 'BankSearch',
  data() {
    return {
      apiKey: this.$root.$data.apiKey,
      map:null,
      latitude:null,
      longitude:null,
      infowindow:null,
      basicControl: null,
      zoomControl: null,
      ps: null,
      bs: null,
      searchKeyword:null,
      bankList: []
    }
  },
  mounted() {
    // const API_KEY = process.env.VUE_APP_KAKAO_API_KEY;

    const script = document.createElement('script');
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${this.apiKey}&autoload=false`
    const scriptForLib = document.createElement('script');
    scriptForLib.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${this.apiKey}&libraries=services,clusterer,drawing&autoload=false`
    /* global kakao */
    script.onload = () => {
      kakao.maps.load(this.fetchLocation)
    }
    document.body.appendChild(script);
    document.body.appendChild(scriptForLib);
  },
  methods: {
    fetchLocation() {
      const compo = this

      const options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0,
      };

      function success(pos) {
        const crd = pos.coords;

        compo.latitude = crd.latitude;
        compo.longitude = crd.longitude;
        compo.createMap()
      }

      function error(err) {
        console.warn(`ERROR(${err.code}): ${err.message}`);
      }

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error, options);
      } else {
        alert("이 브라우저에서는 Geolocation이 지원되지 않습니다.");
      }
    },
    createMap() {
      const container = document.getElementById('map');
      const options = {
        // center: new kakao.maps.LatLng(33.450701, 126.570667),
        center: new kakao.maps.LatLng(this.latitude, this.longitude),
        level: 5
      };

      this.map = new kakao.maps.Map(container, options);
      this.bs = new kakao.maps.services.Places(this.map);
      this.basicControl = new kakao.maps.MapTypeControl();
      this.zoomControl = new kakao.maps.ZoomControl();

      this.map.addControl(this.basicControl, kakao.maps.ControlPosition.TOPRIGHT);
      this.map.addControl(this.zoomControl, kakao.maps.ControlPosition.RIGHT);
      const compo = this
      const kakaoo = kakao.maps

      function placeSearchCB(data, status, pagination) {
        //무슨함수어쩌고
        // console.log(kakaoo.services.Status.OK)
        if (status == kakaoo.services.Status.OK) {

          for (var i = 0; i < data.length; i++) {
            // console.log(data[i]);
            compo.displayMarker(data[i]);
          // this.displayMarker(data[i]);
          }
        }
      }
      this.bs.categorySearch('BK9',placeSearchCB,{useMapBounds:true})
    },
    search() {
      this.ps = new kakao.maps.services.Places();
      
      const compo = this
      const kakaoo = kakao.maps
      console.log(compo.bankList,this.bankList)
      

      function placeSearchCB(data, status, pagination) {
        if (status == kakaoo.services.Status.OK) {
         
          var bounds = new kakao.maps.LatLngBounds();
          console.log('이거목록',data)
          for (var i = 0; i < data.length; i++) {
            
            if (data[i].category_group_code == 'BK9') {
            compo.bankList.push(data[i])
          }
        
            compo.displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
          }
        compo.map.setBounds(bounds);
        
        }
      }

      this.ps.keywordSearch(this.searchKeyword,placeSearchCB)
      this.bankList=[]

    },
    displayMarker(place) {
      const compo = this
      this.infowindow = new kakao.maps.InfoWindow({zIndex:1});
      const marker = new kakao.maps.Marker({
        map: this.map,
        position: new kakao.maps.LatLng(place.y, place.x)
      })
      //마커를 클릭 이벤트에 등록
      kakao.maps.event.addListener(marker, 'click', function() {
        //마커를 클릭하면 장소명이 인포윈도에 출력되게
        compo.infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        compo.infowindow.open(compo.map, marker);
      })
    },
  }
}
</script>

<style scoped>
/* @import "@/assets/css/search.css"; */
/* #map {
  width: 600px;
  height: 500px;
} */
#map {
  width: 100%; 
  height: 500px;
  margin-right: 30px;
}

.map-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
body{
  margin: 0;
  padding: 0;
  background-color: #fff;
}
.search-box{
  padding: 10px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  height: 30px;
  background-color: #fff;
  border: 1px solid #51e3d4;
  border-radius: 30px;
  transition: 0.4s;
  width:30px;
}
.search-box:hover{
  box-shadow: 0px 0px .5px 1px #51e3d4;
  width: 282px;
}
.search-btn{
  text-decoration: none;
  float: right;
  width: 30px;
  height: 30px;
  background-color: #fff;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #51e3d4;
}
.search-box:hover > .search-btn{
  background-color: #fff;
}
.search-txt{
  display: flex;
  padding: 0;
  width: 0px;
  border:none;
  background: none;
  outline: none;
  float: left;
  font-size: 1rem;
  line-height: 30px;
  transition: .4s;
}
.search-box:hover > .search-txt{
  width: 240px;
  padding: 0 6px;
}

</style>
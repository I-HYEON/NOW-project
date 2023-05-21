<template>
  <div>
    <h4>가까운 은행을 검색해보세요</h4>
    <form @submit.prevent="search">
      <input type="text" placeholder="찾고싶은 은행을 입력하세요"  v-model="searchKeyword">
      <input type="submit" value="검색">
    </form>
    <div id="map"></div>
    <div v-if="bankList.length">
      근처에 총 {{ bankList.length }} 개의 은행이 있습니다.
      <hr>
      <div v-for="(bank,index) in bankList" :key="bank.id">
        <ul>
          <li style="list-style-type: none;">{{ index +1 }}번째 은행</li>
          <li>{{ bank.place_name }}</li>
          <li>{{ bank.category_name }}</li>
          <li>{{ bank.phone }}</li>
          <li>{{ bank.road_address_name }}</li>
          <li>{{ bank.place_url }}</li>
        </ul>
        <hr>
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

    },
    displayMarker(place) {
      // console.log('왜 일로 안오지?')
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

<style>
#map {
  width: 600px;
  height: 500px;
}
</style>
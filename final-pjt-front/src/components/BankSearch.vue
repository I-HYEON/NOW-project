<template>
  <div>
    <h4>카카오 맵이 잘나오는지 테스트</h4>
    <div id="map"></div>
  </div>
</template>

<script>

export default {
  name: 'BankSearch',
  data() {
    return {
      map:null,
      cur_lat:null,
      cur_lon:null,
    }
  },
  mounted() {
    // const API_KEY = process.env.VUE_APP_KAKAO_API_KEY;

    if (!window.kakao || !window.kakao.maps) {
      const script = document.createElement('script');
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=7c19c4178f65a36158ee1fad675c95c2&autoload=false`
    
      /* global kakao */
      script.onload = () => {
        kakao.maps.load(this.initMap)
      }
      document.body.appendChild(script);
    }
    else {
      this.initMap()
    }
  },
  methods: {
    temp(){
      const optionss = {
      enableHighAccuracy: true,
      timeout: 5000,
      maximumAge: 0,
      };

      function success(pos) {
        const crd = pos.coords;
        // this.cur_lat = crd.latitude;
        // this.cur_lon = crd.longitude;
        console.log(`Latitude : ${crd.latitude}`);
        console.log(`Longitude: ${crd.longitude}`);
        console.log(`More or less ${crd.accuracy} meters.`);
      }

      function error(err) {
        console.warn(`ERROR(${err.code}): ${err.message}`);
      }

      console.log(navigator.geolocation.getCurrentPosition(success, error, optionss));
    },
    initMap() {
      this.temp()
      const container = document.getElementById('map');
      const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 5
		  };

		  this.map = new kakao.maps.Map(container, options);
    }
  }
}
</script>

<style>
#map {
  width: 600px;
  height: 500px;
}
</style>
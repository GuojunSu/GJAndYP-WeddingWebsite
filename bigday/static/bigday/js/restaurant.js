<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@8"></script>
<script>
$(document).ready(function() {
    var Mode;
    $(".dropdown-menu li a").click(function() {
        if ($(this).parents("#_dropdown").find('.btn').length > 0) {
            $(this).parents("#_dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
            Mode = $(this).data('value');
        }
    });

    $("#submit").click(function() {
        var sJson = JSON.stringify({
            "Departure": $("#_destination").val(),
            "Mode": Mode
        });

         Swal.fire({
            title: '收巡路徑',
            text: '請等待...',
            type: 'warning',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: 'Search',
            showLoaderOnConfirm: true,
            preConfirm: function() {
                return new Promise(function(resolve) {
                     $.ajax({
                        url: 'http://127.0.0.1:8000/api/execGoogleApiTask',
                        type: "post",
                        timeout: 5000,
                        data: sJson,
                        contentType: 'application/json; charset=utf-8',
                        success: function(result) {
                            SetDirectionTimer(result.task_id, resolve);
                        },
                        complete: function(data) {},
                        error: function(data) {
                        }
                    });
                });
            },
            allowOutsideClick: false
        }).then((result) => {
           Swal.fire({
               type: 'success',
               title: 'Ajax请求完成！',
           });
        });
    });
})

function SetDirectionTimer(taskId, resolve) {
    var timer = setInterval(function() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/getResult/' + taskId,
            type: "GET",
            success: function(response) {
                var taskStatus = response.task_status;
                if (taskStatus === 'SUCCESS') {
                    clearTimer();
                    setMaps(response.results);
                    resolve('okay');
                } else if (taskStatus === 'FAILURE') {
                    clearTimer();
                }
            },
            error: function(err) {
                console.log('err', err);
                clearTimer();
            }
        });
    }, 1000);

    function setMaps(resp) {
        // 繪製路線
        result = JSON.parse(resp);
        map = new google.maps.Map(document.getElementById('map'), {
            zoom: 16,
            center: {
                lat: 25.034010,
                lng: 121.562428
            }
        });
        // Create a renderer for directions and bind it to the map.
        var directionsRenderer = new google.maps.DirectionsRenderer({
            map: map
        });
        var steps = result.routes[0].legs[0].steps;
        var markers = [];
        var infowindows = [];
        steps.forEach((e, i) => {
            // 加入地圖標記
            markers[i] = new google.maps.Marker({
                position: {
                    lat: e.start_location.lat,
                    lng: e.start_location.lng
                },
                map: map,
                label: {
                    text: i + '',
                    color: "#fff"
                }
            });
            // 加入資訊視窗
            infowindows[i] = new google.maps.InfoWindow({
                content: e.instructions,
                maxWidth: 200,
                pixelOffset: new google.maps.Size(100, -20)
            });
            // 加入地圖標記點擊事件
            markers[i].addListener('click', function() {
                if (infowindows[i].anchor) {
                    infowindows[i].close();
                } else {
                    infowindows[i].open(map, markers[i]);
                }
            });
        });
        directionsRenderer.setDirections(result);
    }

    function clearTimer() {
        console.log('close Timer');
        clearInterval(timer);
    }
}
</script>
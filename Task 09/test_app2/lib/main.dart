import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:flutter_osm_plugin/flutter_osm_plugin.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:osm_flutter_hooks/osm_flutter_hooks.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Geo quest',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const MyHomePage(title: 'Geo Quest'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  // final GlobalKey<MyHomePageState> key = GlobalKey();
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late _SimpleOSMController osmController;

  @override
  void initState() {
    super.initState();
    osmController = _SimpleOSMController();
    setState(() {});
  }

  void _resetMap() {
    osmController.removeLastRoad();
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: _SimpleOSM(
        controller: osmController,
      ),
      bottomNavigationBar: Container(
        alignment: Alignment.center,
        height: 70,
        color: Colors.white,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            ValueListenableBuilder<double>(
              valueListenable: osmController.durationNotifier,
              builder: (context, newDuration, child) {
                return Text('Duration: ${newDuration.toStringAsFixed(2)}');
              },
            ),
            ElevatedButton(
              onPressed: () {
                debugPrint('ElevatedButton Clicked');
                _resetMap(); // Call the reset function on button click.
              },
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(50),
                ),
                minimumSize: const Size(50, 50),
              ),
              child: const Text('X'),
            ),
            ValueListenableBuilder<double>(
              valueListenable: osmController.distanceNotifier,
              builder: (context, newDistance, child) {
                return Text('Distance: ${newDistance.toStringAsFixed(2)}');
              },
            ),
          ],
        ),
      ),
    );
  }
}

class _SimpleOSMController {
  late MapController controller;
  // double distance = 0.0;
  // double duration = 0.0;
  final ValueNotifier<double> distanceNotifier = ValueNotifier<double>(0.0);

  final ValueNotifier<double> durationNotifier = ValueNotifier<double>(0.0);

  void initializeController(MapController mapController) {
    controller = mapController;
  }

  void updateDistance(double newDistance) {
    setState(() {
      distanceNotifier.value = newDistance;
    });
  }

  void updateDuration(double newDuration) {
    setState(() {
      durationNotifier.value = newDuration;
    });
  }

  void removeLastRoad() {
    controller.removeLastRoad();
    updateDistance(0.0);
    updateDuration(0.0);
  }

  void setState(VoidCallback fn) {
    fn();
  }
}

class _SimpleOSM extends HookWidget {
  final _SimpleOSMController controller;

  const _SimpleOSM({required this.controller});

  @override
  Widget build(BuildContext context) {
    final mapController = useMapController(
      userTrackingOption: const UserTrackingOption(
        enableTracking: true,
        unFollowUser: true,
      ),
    );

    useMapIsReady(
      controller: mapController,
      mapIsReady: () async {
        await mapController.setZoom(zoomLevel: 15);
      },
    );

    useMapListener(
      controller: mapController,
      onSingleTap: (p) async {
        final userLocation = await mapController.myLocation();
        await mapController.addMarker(p,
            markerIcon: const MarkerIcon(
              icon: Icon(
                Icons.pin_drop,
                color: Colors.black,
                size: 35,
              ),
            ));

        final roadInfo = await mapController.drawRoad(
          userLocation,
          p,
          roadType: RoadType.car,
          roadOption: const RoadOption(
            roadWidth: 10,
            roadColor: Colors.blue,
            zoomInto: true,
          ),
        );

        var newDistance = roadInfo.distance;
        var newDuration = roadInfo.duration;
        var durationThree = Duration(minutes: 0, seconds: newDuration!.toInt());

        controller.updateDistance(newDistance!);
        controller.updateDuration(newDuration);

        print("Distance-$newDistance");
        print(durationThree);
      },
    );

    useMapListener(
      controller: mapController,
      onSingleTap: (p) async {
        mapController.removeLastRoad();
      },
    );

    controller.initializeController(mapController);

    return OSMFlutter(
      osmOption: OSMOption(
        userTrackingOption: const UserTrackingOption(
          enableTracking: true,
          unFollowUser: false,
        ),
        zoomOption: const ZoomOption(
          initZoom: 11,
          minZoomLevel: 3,
          maxZoomLevel: 19,
          stepZoom: 1.0,
        ),
        userLocationMarker: UserLocationMaker(
          personMarker: const MarkerIcon(
            icon: Icon(
              Icons.location_history_rounded,
              color: Colors.red,
              size: 45,
            ),
          ),
          directionArrowMarker: const MarkerIcon(
            icon: Icon(
              Icons.double_arrow,
              size: 48,
            ),
          ),
        ),
        roadConfiguration: const RoadOption(
          roadColor: Colors.yellowAccent,
        ),
        markerOption: MarkerOption(
          defaultMarker: const MarkerIcon(
            icon: Icon(
              Icons.person_pin_circle,
              color: Colors.red,
              size: 45,
            ),
          ),
        ),
      ),
      controller: mapController,
      mapIsLoading: const Center(
        child: SpinKitWaveSpinner(
          color: Colors.green,
          size: 85,
        ),
      ),
    );
  }
}
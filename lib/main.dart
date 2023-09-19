import 'dart:developer';

import 'package:cloud_functions/cloud_functions.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:reading_memo/firebase_options.dart';
import 'package:http/http.dart' as http;

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

void helloWorld() async {
  try {
    final url =
        "https://asia-northeast1-reading-memo-67bb8.cloudfunctions.net/testFunction";
    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      print('Response data: ${response.body}');
    } else {
      print(
          'Failed to call cloud function. Status code: ${response.statusCode}');
    }
  } on FirebaseFunctionsException catch (e) {
    log(e.code);
    log(e.details ?? "null");
    log(e.message ?? "message is null");
  }
}

Future<void> callAddMessageFunction(String text) async {
  final url =
      'https://us-central1-reading-memo-67bb8.cloudfunctions.net/addMessage?text=$text';

  final response = await http.get(Uri.parse(url));

  if (response.statusCode == 200) {
    print('Response data: ${response.body}');
  } else {
    print('Failed to call cloud function. Status code: ${response.statusCode}');
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("サンプル")),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            callAddMessageFunction("Your message text here");
          },
          child: const Text("say hello world"),
        ),
      ),
    );
  }
}

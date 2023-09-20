import 'dart:developer';

import 'package:cloud_functions/cloud_functions.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
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
    const url =
        "https://asia-northeast1-reading-memo-67bb8.cloudfunctions.net/testFunction";
    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      log('Response data: ${response.body}');
    } else {
      log('Failed to call cloud function. Status code: ${response.statusCode}');
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
    log('Response data: ${response.body}');
  } else {
    log('Failed to call cloud function. Status code: ${response.statusCode}');
  }
}

Future<void> changeToMemo({required String text}) async {
  final url =
      "https://us-central1-reading-memo-67bb8.cloudfunctions.net/changeToMemo?text=$text";
  final response = await http.get(Uri.parse(url));
  if (response.statusCode == 200) {
    log('Response data: ${response.body}');
  } else {
    log('Failed to call cloud function. Status code: ${response.statusCode}');
  }
}

// final formattedTextProvider = StateProvider<String>((ref) => "");

// Future<void> changeToMemoWithSudachi({required String text}) async {
//   final url =
//       "https://us-central1-reading-memo-67bb8.cloudfunctions.net/changeToMemoWithSudachi?text=$text";
//   final response = await http.get(Uri.parse(url));
//   print("response : $response");
//   print("response.body : ${response.body}");
//   if (response.statusCode == 200) {
//     log('Response data: ${response.body}');
//   } else {
//     log('Failed to call cloud function. Status code: ${response.statusCode}');
//   }
// }

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

final formattedTextProvider = StateProvider<String>((ref) => "");

class MyHomePage extends HookConsumerWidget {
  const MyHomePage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    Future<void> changeToMemoWithSudachi({required String text}) async {
      final url =
          "https://us-central1-reading-memo-67bb8.cloudfunctions.net/changeToMemoWithSudachi?text=$text";
      final response = await http.get(Uri.parse(url));
      ref.watch(formattedTextProvider.notifier).state = response.body;
      print("response : $response");
      print("response.body : ${response.body}");
      if (response.statusCode == 200) {
        log('Response data: ${response.body}');
      } else {
        log('Failed to call cloud function. Status code: ${response.statusCode}');
      }
    }

    return Scaffold(
      appBar: AppBar(title: const Text("サンプル")),
      body: Center(
        child: Column(
          children: [
            ElevatedButton(
              onPressed: () {
                changeToMemoWithSudachi(text: "アインシュタインは相対性理論を発見して、ベロを出した天才科学者です。");
              },
              child: const Text("change to memo"),
            ),
            Text(ref.watch(formattedTextProvider.notifier).state),
          ],
        ),
      ),
    );
  }
}

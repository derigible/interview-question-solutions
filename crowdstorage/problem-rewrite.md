# The Problem

There are two programs that cannot establish a direct connection to each other. Write a generic TCP relay server that these two programs can use to send data back and forth. This is common in peer-to-peer networks where one peer cannot talk to another peer, but both peers can talk to a third party (ie the relay server).

## Requirements

1. Implement a relay server program that listens for requests over a TCP connection on a given port (for example, port 8080) that will return a (host, port) pair to the requesting client. The relay server should then be able to forward traffic from any program that connects to that (host, port) to the requesting client.
1. Any program should be able to take the (host, port) as parameters to talk to the requesting client (via the relay). Assume these programs are not under your control and cannot be modified. An example program might be telnet.
1. The requesting client is a program that you can assume is under your control, so any modifications necessary to contact the relayserver can be done.
1. As part of this assignment, write a client that will use the relay server. This client should output the (host, pair) it received from the relay server so that we can connect to it with programs like telnet.

    We suggest writing a client that, after establishing a relay connection with the relay server, simply sends back any data it receives (echoes it back). This will also be an easy way to test if your connection is working from programs like telnet or netcat. We recommend calling it `echoserver`, but it can be whatever you want.
1. The relay server should be able to handle concurrent requesting clients. It should also be able to relay concurrent TCP connections on a given (host, port) to the correct requesting client (for example, the requesting client is an http server and multiple browsers are attempting to communicate with that server).
1. We're looking for something that could reasonably be considered "production quality." We're interested in hearing from you what things are important to do and consider because of this criteria.

## Examples

An example of how the programs might work is as follows:

### Relay Server

The relay server will listen on a port for requesting clients to establish a relay, and so at a minimum will need to accept a port as an argument:

```
./relay port
```

You may accept other arguments for the relay server as needed.

### Requesting Client (echoserver)

Your requesting client should be started on the command line and accept arguments to connect to the relay server.

```
./echoserver relayhost relayport
```

`relayhost` is the host the relay is running on and `relayport` is the port provided to the relay server.

### Example Session

```
$ ./relay 8080 &
$ ./echoserver localhost 8080 &
established relay address: (localhost, 8081)
$ telnet localhost 8081
Hello, world!  # entered by user
Hello, world!  # response back from echoserver
```

## Considerations

1. Data sent does not need to be of any particular protocol and could even be binary. Do not assume any format or type to the data for the client you write.
1. TCP is what many application layer protocols are built on top of - do not mix up TCP with higher level protocols like websockets (which is built on top of TCP).
1. You may use whatever language and tools are most comfortable for you, though we ask you try to limit yourself to standard libraries where possible.

## Ask Questions!

This homework problem is written to be challenging. There might be terms or systems you are unfamiliar with so feel free to ask questions. What we're interested in is how you tackle and solve problems, especially problems you haven't seen before. This problem might require some research and certainly some questions and clarification from us.

Please don't get stuck! If you get stuck, just let us know and we'll be more than happy to provide help of any kind. The best way to ask us questions it through the slack channel that we have set up. We will try to be as responsive as we can. Note that part of what we are considering is not just how you solve problems, but it is how you work through problems with the team.

Not everyone we've hired has completely solved this problem so don't let that discourage you. We care more about the approach and the process than the answer.​

## Submission

When you're done, please submit what you have via our Slack channel. Remember, it doesn't need to be complete.

import grpc
import proto.kubearmor_pb2 as kubearmor_pb2
import proto.kubearmor_pb2_grpc as kubearmor_pb2_grpc


def run_client():
    channel = grpc.insecure_channel('localhost:50051')

    # Create stubs
    log_stub = kubearmor_pb2_grpc.LogServiceStub(channel)
    push_log_stub = kubearmor_pb2_grpc.PushLogServiceStub(channel)

    # HealthCheck example
    health_check_response = log_stub.HealthCheck(kubearmor_pb2.RequestMessage(nonce=123))
    print("HealthCheck Response:", health_check_response.Retval)

    # WatchMessages example (not implemented in the server, just for demonstration)
    messages_response = log_stub.WatchMessages(kubearmor_pb2.RequestMessage(nonce=456))
    for message in messages_response:
        print("Received Message:", message)

    # PushMessages example
    push_message_response = push_log_stub.PushMessages(iter([kubearmor_pb2.Message()]))
    print("PushMessages Response:", push_message_response.Retval)

    # WatchLogs example
    watch_logs_response = log_stub.WatchLogs(kubearmor_pb2.LogFilter(Filter="all"))
    for log in watch_logs_response:
        print("Received Log:", log)

    # PushLogs example
    push_logs_response = push_log_stub.PushLogs(iter([kubearmor_pb2.Log()]))
    print("PushLogs Response:", push_logs_response.Retval)


if __name__ == '__main__':
    run_client()

import argparse
import grpc
import proto.kubearmor_pb2 as kubearmor_pb2
import proto.kubearmor_pb2_grpc as kubearmor_pb2_grpc


def __create_connection(conn:str='localhost:50051')->kubearmor_pb2_grpc.LogServiceStub:
    """
    Based on connection information, create a channel and stub
    """
    channel = grpc.insecure_channel('localhost:50051')
    stub = kubearmor_pb2_grpc.LogServiceStub(channel)

    return stub


def __health_check(stub:kubearmor_pb2_grpc.LogServiceStub):
    """
    Check connectivity to gRPC server
    """
    status = False
    nonce_message = kubearmor_pb2.NonceMessage(nonce=15)
    health_check_response = stub.HealthCheck(nonce_message)

    if health_check_response.Retval == 15:
        status = True
    return status


def run_client():
    parse = argparse.ArgumentParser()
    parse.add_argument("--conn", type=str, default='localhost:50051', help='Connection information')
    args = parse.parse_args()

    stub = __create_connection(conn=args.conn)

    # check whether it's able to send a HealthCheck against server
    status = __health_check(stub=stub)
    if status is True:
        print(f"Successfully sent a healthcheck message against gRPC server")
    else:
        print(f"Failed to send a healthcheck message against gRPC server")
        exit(1)

    request_message = kubearmor_pb2.RequestMessage(Filter='all')
    watch_logs_response = stub.WatchLogs(request_message)

    # Returns Stack script
    for entry in watch_logs_response:
        print(str(entry))




if __name__ == '__main__':
    run_client()
